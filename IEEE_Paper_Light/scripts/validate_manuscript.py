"""Check statistical identities, invalid inputs, references, and rendered light figures."""
from pathlib import Path
import hashlib
import json
import re
import numpy as np
import pandas as pd
import fitz
from prepare_manuscript import fixed_target_gaps, MODELS, DOMAINS, CLASSES

ROOT=Path(__file__).resolve().parents[1]

def main():
    checks=[]
    raw=pd.read_csv(ROOT/'data/all_metrics.csv')
    assert len(raw)==72 and set(raw.model)==set(MODELS)
    assert raw.groupby('subset').size().to_dict()=={'clean_only':36,'full':36}
    assert set(raw.seed)=={13,37,71}
    for _,r in raw.iterrows():
        assert np.isclose(r.map50_95,np.mean([r[c+'_ap50_95'] for c in CLASSES]),atol=1e-12)
    checks.append('72 raw metric rows, 18 runs, four-class mAP identity')
    summary=pd.read_csv(ROOT/'data/metric_summary.csv')
    for _,r in summary.iterrows():
        q=raw[(raw.model==r.model)&(raw.train==r.train)&(raw.target==r.target)&(raw.subset==r.subset)]
        assert len(q)==3
        for key in ['map50','map50_95']+[c+'_ap50_95' for c in CLASSES]:
            assert np.isclose(r[key+'_mean'],100*q[key].mean(),atol=1e-10)
            assert np.isclose(r[key+'_sd'],100*q[key].std(ddof=1),atol=1e-10)
    checks.append('All saved means and sample SDs independently match raw metrics')
    gaps=fixed_target_gaps(raw)
    for subset in ['full','clean_only']:
        assert (gaps[gaps.subset==subset].gap_pp>0).all()
    q=gaps[(gaps.model=='YOLO26n')&(gaps.subset=='full')]
    assert np.isclose(q[q.target=='Drone'].gap_pp.mean(),16.905667,atol=1e-6)
    assert np.isclose(q[q.target=='MotorBike'].gap_pp.mean(),42.269058,atol=1e-6)
    assert not np.isclose(q[q.target=='Drone'].gap_pp.mean(),12.00,atol=.01)
    checks.append('Fixed-target YOLO26 gap regression; all full and clean-only seed gaps positive')
    # Negative tests: duplicate archive rows and missing same-target baselines must fail.
    invalid=[pd.concat([raw,raw.iloc[[0]]],ignore_index=True),raw.drop(raw.index[0])]
    for bad in invalid:
        try:fixed_target_gaps(bad)
        except ValueError:pass
        else:raise AssertionError('Invalid metric table unexpectedly accepted')
    checks.append('Negative tests reject duplicate rows and missing fixed-target baselines')

    train=pd.read_csv(ROOT/'data/training_audit.csv')
    assert len(train)==18 and (train.epochs==150).all() and (train.patience==0).all()
    assert set(train.ultralytics)=={'8.4.190'}
    for _,r in train.iterrows():
        f=pd.read_csv(ROOT/f'data/training_logs/{r.model}_{r.train}_{r.seed}.csv')
        assert f.epoch.tolist()==list(range(1,151))
        assert int(f.loc[f['metrics/mAP50-95(B)'].idxmax(),'epoch'])==r.best_map_epoch
    checks.append('18 retained training CSVs have 150 epochs and the stated validation peaks')

    included=[]
    for stem in ['main','supplement']:
        tex=(ROOT/f'{stem}.tex').read_text()
        labels=set(re.findall(r'\\label\{([^}]+)\}',tex))
        refs=set(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',tex))
        assert refs<=labels,(stem,refs-labels)
        included.extend(re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',tex))
        pdf=fitz.open(ROOT/f'{stem}.pdf')
        text='\n'.join(p.get_text() for p in pdf)
        assert '??' not in text
        assert all(m in text for m in MODELS)
        log=(ROOT/f'build/{stem}.log').read_text()
        for pattern in [r'Citation .* undefined',r'Reference .* undefined',r'There were undefined references',r'Missing character:',r'^!']:
            assert not re.search(pattern,log,re.MULTILINE),(stem,pattern)
        hboxes=[float(x) for x in re.findall(r'Overfull \\hbox \(([\d.]+)pt too wide\)',log)]
        assert not hboxes or max(hboxes)<1.0,(stem,hboxes)
        checks.append(f'{stem}.pdf: {len(pdf)} pages, resolved labels/citations, no missing glyphs or material horizontal overflow')
    assert len(included)==len(set(included))==3
    assert len(list((ROOT/'figures').glob('*.pdf')))==4
    digests=[]
    for p in (ROOT/'figures').glob('*.pdf'):
        assert p.name.endswith('_light.pdf')
        digests.append(hashlib.sha256(p.read_bytes()).hexdigest())
        doc=fitz.open(p);pix=doc[0].get_pixmap(matrix=fitz.Matrix(1,1),alpha=False)
        a=np.frombuffer(pix.samples,dtype=np.uint8).reshape(pix.height,pix.width,pix.n)[:,:,:3]
        # White outer border verifies the actual rendered figure, not only its filename.
        border=np.concatenate([a[:2].reshape(-1,3),a[-2:].reshape(-1,3),a[:,:2].reshape(-1,3),a[:,-2:].reshape(-1,3)])
        assert (border>=245).all(axis=1).mean()>.98,p.name
    assert len(set(digests))==4
    checks.append('Three distinct figure inclusions plus one optional plot; all four rendered backgrounds are white; no dark assets')
    result={'status':'passed','checks':checks,'scope':'Archived-metric reanalysis and manuscript artifact validation; no new training/inference'}
    (ROOT/'build/validation.json').write_text(json.dumps(result,indent=2))
    for x in checks:print('PASS:',x)

if __name__=='__main__':main()
