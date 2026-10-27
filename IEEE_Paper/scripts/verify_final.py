"""Verify the actual final source against raw retained metric records and baseline."""
from pathlib import Path
import re
import json
import hashlib
import numpy as np
import pandas as pd
import fitz

ROOT=Path(__file__).resolve().parents[1]
MODELS=['YOLO11n','YOLOv8n','YOLO26n']
DOMAINS=['Drone','MotorBike']
SEEDS=[13,37,71]
CLASSES=['D00','D10','D20','D40']

def calculate_gaps(raw):
    if raw.duplicated(['model','train','target','seed','subset']).any():raise ValueError('Duplicate observations')
    result=[]
    for (subset,model,target,seed),q in raw.groupby(['subset','model','target','seed']):
        a=q[q.train==target];b=q[q.train!=target]
        if len(a)!=1 or len(b)!=1:raise ValueError('Missing same-target comparator')
        result.append(dict(subset=subset,model=model,target=target,seed=seed,gap=(a.map50_95.iloc[0]-b.map50_95.iloc[0])*100))
    return pd.DataFrame(result)

def main():
    checks=[]
    raw=pd.read_csv(ROOT/'data/all_metrics.csv')
    assert len(raw)==72 and len(raw[raw.subset=='full'])==36
    assert set(raw.model)==set(MODELS) and set(raw.seed)==set(SEEDS)
    assert set(raw.split_manifest_sha256)=={'55c87dabc5da1ef500560648ec40717cde381dec0410b3abab83cbdfceed1322'}
    for _,row in raw.iterrows():assert np.isclose(row.map50_95,np.mean([row[c+'_ap50_95'] for c in CLASSES]),atol=1e-12)
    gaps=calculate_gaps(raw)
    assert len(gaps)==36 and (gaps.gap>0).all()
    for bad in [pd.concat([raw,raw.iloc[[0]]],ignore_index=True),raw.drop(raw.index[0])]:
        try:calculate_gaps(bad)
        except ValueError:pass
        else:raise AssertionError('Invalid pair records accepted')
    checks.append('72 real metric rows and four-class mAP identity; all full/clean paired gaps positive; negative duplicate/missing-baseline tests passed')
    source=(ROOT/'main.tex').read_text();baseline=(ROOT/'provenance/before_yolo26/main.tex').read_text()
    for token in ['title','author']:
        # These declarations are single source lines in this project.
        b=next(x for x in baseline.splitlines() if x.startswith('\\'+token+'{'))
        assert b in source,f'Changed original {token}'
    for m in re.findall(r'\\begin\{(?:equation|align)\}.*?\\end\{(?:equation|align)\}',baseline,re.S):assert m in source
    base_labels=set(re.findall(r'\\label\{([^}]+)\}',baseline));labels=re.findall(r'\\label\{([^}]+)\}',source)
    assert base_labels<=set(labels) and len(labels)==len(set(labels))
    assert set(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',source))<=set(labels)
    base_cites=set(k.strip() for block in re.findall(r'\\cite\{([^}]+)\}',baseline) for k in block.split(','))
    cites=set(k.strip() for block in re.findall(r'\\cite\{([^}]+)\}',source) for k in block.split(','))
    assert base_cites<=cites and cites-base_cites=={'ultralyticsyolo26'}
    checks.append('Original title, authors, equation structures, labels and all cited keys retained; only YOLO26 citation added')
    blocks=re.findall(r'\\begin\{table\*?\}.*?\\end\{table\*?\}',source,re.S)
    assert len(blocks)==7
    def block(label):return next(x for x in blocks if r'\label{'+label+'}' in x)
    def assert_rows(label,expected):
        b=block(label)
        body=b.split(r'\midrule',1)[1].split(r'\bottomrule',1)[0]
        got=[x.strip() for x in body.split(r'\\') if x.strip()]
        assert got==expected,(label,got,expected)
    full=raw[raw.subset=='full']
    def pm(q,key):return f'${q[key].mean()*100:.2f}\\pm{q[key].std(ddof=1)*100:.2f}$'
    matrix=[];map50=[];classrows=[];gaprows=[];seedrows=[]
    for model in MODELS:
        for i,train in enumerate(DOMAINS):
            groups=[full[(full.model==model)&(full.train==train)&(full.target==target)] for target in DOMAINS]
            matrix.append(' & '.join([r'\multirow{2}{*}{'+model+'}' if i==0 else '',train,*[pm(q,'map50_95') for q in groups],'3']))
            map50.append(' & '.join([model,train,*[pm(q,'map50') for q in groups]]))
        vals=[]
        for target in DOMAINS:
            q=gaps[(gaps.model==model)&(gaps.target==target)&(gaps.subset=='full')]
            vals.append(f'${q.gap.mean():.2f}\\pm{q.gap.std(ddof=1):.2f}$')
            s=q.set_index('seed')
            seedrows.append(' & '.join([model,target,*[f'{s.loc[seed,"gap"]:.2f}' for seed in SEEDS]]))
        gaprows.append(' & '.join([model,*vals]))
    for target in DOMAINS:
        for model in MODELS:
            for train in DOMAINS:
                q=full[(full.model==model)&(full.train==train)&(full.target==target)]
                classrows.append(' & '.join([model,train,target,*[f'{q[c+"_ap50_95"].mean()*100:.2f}' for c in CLASSES]]))
    for label,rows in [('tab:matrix',matrix),('tab:map50',map50),('tab:paired',gaprows),('tab:seeds',seedrows),('tab:classap',classrows)]:
        # Ignore the intentionally empty first model cell on second multirow rows.
        assert_rows(label,[x.strip() for x in rows])
    for label in ['tab:counts','tab:boxes']:
        old=next(x for x in re.findall(r'\\begin\{table\*?\}.*?\\end\{table\*?\}',baseline,re.S) if r'\label{'+label+'}' in x)
        assert block(label)==old
    checks.append('All five metric-table bodies independently match raw observations; original count/support tables are byte-identical')
    for marker in ['RQ1','RQ2','RQ3','RQ4','Consensus:','Trade-off:','Gap:','This paper.','YOLO family evolution.','Why does performance degrade?','Comparison with prior work.',r'\subsection{Limitations}',r'\subsection{Threats to Validity}']:
        assert marker in source,marker
    assert 'supplement' not in source.lower()
    figures=re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',source)
    assert len(figures)==len(set(figures))==4
    for rel in figures:
        p=ROOT/rel
        doc=fitz.open(p);pix=doc[0].get_pixmap(alpha=False)
        arr=np.frombuffer(pix.samples,dtype=np.uint8).reshape(pix.height,pix.width,pix.n)
        assert (arr[0,:,:3]>=245).all()
        stem=p.stem
        collision=json.loads((ROOT/f'qa/figures/{stem}.collision.json').read_text())
        alignment=json.loads((ROOT/f'qa/figures/{stem}.alignment.json').read_text())
        assert collision['verdict']=='PASS' and alignment['verdict'] in ['PASS','NOT APPLICABLE']
    checks.append('Four agreed RQs, original argument chain, seven main-paper tables and four distinct light figures; rendered alignment/collision audits passed')
    pdf=fitz.open(ROOT/'main.pdf');text='\n'.join(p.get_text() for p in pdf)
    assert '??' not in text and all(m in text for m in MODELS)
    log=(ROOT/'build/main.log').read_text()
    for pattern in ['There were undefined references','Missing character:','multiply defined']:
        assert pattern not in log
    hboxes=[float(x) for x in re.findall(r'Overfull \\hbox \(([\d.]+)pt too wide\)',log)]
    assert not hboxes or max(hboxes)<1
    checks.append(f'Compiled {len(pdf)}-page PDF: resolved citations/labels, no missing glyphs or material horizontal overflow')
    result={'status':'passed','checks':checks,'scope':'Source integration, archived-metric recomputation and compiled artifact QA; not independent training/inference or raw-scene audit'}
    (ROOT/'qa/verification.json').write_text(json.dumps(result,indent=2))
    for item in checks:print('PASS:',item)

if __name__=='__main__':main()
