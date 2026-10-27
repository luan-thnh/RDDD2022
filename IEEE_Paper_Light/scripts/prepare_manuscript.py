"""Generate manuscript tables and light figures from audited archive metrics.

Run from any directory: python3 scripts/prepare_manuscript.py
Does not load model weights, retrain models, or rerun inference.
"""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/rdd2022-light-mpl')
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
MODELS = ['YOLOv8n', 'YOLO11n', 'YOLO26n']
DOMAINS = ['Drone', 'MotorBike']
CLASSES = ['D00', 'D10', 'D20', 'D40']
COLORS = ['#2874A6', '#D18124', '#27836C']

def fixed_target_gaps(frame):
    keys = ['model', 'train', 'target', 'seed', 'subset']
    if frame.duplicated(keys).any():
        raise ValueError('Duplicate model/source/target/seed/subset metric rows')
    out = []
    for (subset, model, target, seed), group in frame.groupby(['subset', 'model', 'target', 'seed']):
        a = group[group.train == target]
        b = group[group.train != target]
        if len(a) != 1 or len(b) != 1:
            raise ValueError('A fixed-target comparison requires both training domains')
        rec = dict(subset=subset, model=model, target=target, seed=seed,
                   gap_pp=100*(a.map50_95.iloc[0]-b.map50_95.iloc[0]))
        for c in CLASSES:
            rec[c] = 100*(a[c+'_ap50_95'].iloc[0]-b[c+'_ap50_95'].iloc[0])
        out.append(rec)
    return pd.DataFrame(out)

def pm(mean, sd):
    return f'${mean:.2f}\\pm{sd:.2f}$'

def table_file(name, rows):
    (ROOT/'tables'/name).write_text('\n'.join(' & '.join(map(str,r))+r' \\' for r in rows)+'\n\\bottomrule\n')

def save(fig, stem):
    fig.savefig(ROOT/'figures'/f'{stem}.pdf', facecolor='white', bbox_inches='tight')
    fig.savefig(ROOT/'figures'/f'{stem}.png', dpi=300, facecolor='white', bbox_inches='tight')
    plt.close(fig)

def main():
    data = pd.read_csv(ROOT/'data/all_metrics.csv')
    gaps = fixed_target_gaps(data)
    assert len(data) == 72 and len(gaps) == 36
    summary = pd.read_csv(ROOT/'data/metric_summary.csv')
    full = summary[summary.subset == 'full']
    gap_summary = gaps.groupby(['subset','model','target']).gap_pp.agg(['mean','std'])
    fullg = gaps[gaps.subset=='full']
    # Main performance matrix, full-test mAP@50:95.
    rows = []
    for model in MODELS:
        for train in DOMAINS:
            q=full[(full.model==model)&(full.train==train)].set_index('target')
            rows.append([model,train,*[pm(q.loc[t,'map50_95_mean'],q.loc[t,'map50_95_sd']) for t in DOMAINS]])
    table_file('matrix.tex',rows)
    rows=[]
    for model in MODELS:
        cells=[]
        for target in DOMAINS:
            q=gap_summary.loc[('full',model,target)];cells.append(pm(q['mean'],q['std']))
        asym=gap_summary.loc[('full',model,'MotorBike'),'mean']-gap_summary.loc[('full',model,'Drone'),'mean']
        rows.append([model,*cells,f'{asym:.2f}'])
    table_file('gaps.tex',rows)
    rows=[]
    for target in DOMAINS:
        for model in MODELS:
            for train in DOMAINS:
                q=full[(full.model==model)&(full.target==target)&(full.train==train)].iloc[0]
                rows.append([model,train,target,*[f'{q[c+"_ap50_95_mean"]:.2f}' for c in CLASSES]])
    table_file('class_ap.tex',rows)
    for subset,name,metric in [('full','map50.tex','map50'),('clean_only','clean_matrix.tex','map50_95')]:
        rows=[]
        for model in MODELS:
            for train in DOMAINS:
                q=summary[(summary.subset==subset)&(summary.model==model)&(summary.train==train)].set_index('target')
                rows.append([model,train,*[pm(q.loc[t,metric+'_mean'],q.loc[t,metric+'_sd']) for t in DOMAINS]])
        table_file(name,rows)
    rows=[]
    for model in MODELS:
        for target in DOMAINS:
            q=fullg[(fullg.model==model)&(fullg.target==target)].set_index('seed')
            rows.append([model,target,*[f'{q.loc[s,"gap_pp"]:.2f}' for s in [13,37,71]]])
    table_file('seed_gaps.tex',rows)
    train=pd.read_csv(ROOT/'data/training_audit.csv')
    rows=[]
    for model in MODELS:
        for domain in DOMAINS:
            q=train[(train.model==model)&(train.train==domain)].set_index('seed')
            rows.append([model,domain,*[int(q.loc[s,'best_map_epoch']) for s in [13,37,71]]])
    table_file('peak_epochs.tex',rows)

    plt.style.use('default')
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':8,'axes.titlesize':9,
                         'axes.labelsize':8,'xtick.labelsize':8,'ytick.labelsize':8,
                         'legend.fontsize':7,'figure.facecolor':'white','axes.facecolor':'white',
                         'savefig.facecolor':'white','text.color':'#111111','axes.labelcolor':'#111111',
                         'pdf.fonttype':42,'ps.fonttype':42,'axes.spines.top':False,'axes.spines.right':False})
    fig,axes=plt.subplots(1,2,figsize=(7.16,2.7),sharey=True)
    for ax,target in zip(axes,DOMAINS):
        for i,train_domain in enumerate([target,next(d for d in DOMAINS if d!=target)]):
            q=full[(full.train==train_domain)&(full.target==target)].set_index('model').loc[MODELS]
            bars=ax.bar(np.arange(3)+(i-.5)*.34,q.map50_95_mean,.34,yerr=q.map50_95_sd,capsize=2,
                        label=f'Train {train_domain}',color=[COLORS[0],COLORS[1]][i],edgecolor='white',hatch=['','//'][i])
            ax.bar_label(bars,fmt='%.2f',padding=4,fontsize=6.5)
        ax.set_xticks(range(3),MODELS);ax.set_title(f'Fixed target: {target} Test');ax.set_ylim(0,65)
        ax.set_axisbelow(True);ax.grid(axis='y',alpha=.18);ax.legend(loc='upper left',frameon=False)
    axes[0].set_ylabel('mAP@50:95 (%)');fig.tight_layout(pad=.7,w_pad=1.3);save(fig,'fixed_target_comparison_light')

    fig,axes=plt.subplots(1,2,figsize=(7.16,2.7),sharey=True)
    for ax,target in zip(axes,DOMAINS):
        for i,model in enumerate(MODELS):
            q=fullg[(fullg.model==model)&(fullg.target==target)]
            ax.bar(np.arange(4)+(i-1)*.24,[q[c].mean() for c in CLASSES],.24,
                   yerr=[q[c].std(ddof=1) for c in CLASSES],capsize=1.6,
                   color=COLORS[i],hatch=['','//','..'][i],edgecolor='white',linewidth=.5,label=model)
        ax.axhline(0,color='#333333',lw=.7);ax.set_xticks(range(4),CLASSES);ax.set_title(f'Fixed target: {target} Test')
        ax.set_axisbelow(True);ax.grid(axis='y',alpha=.18);ax.set_ylim(-25,70)
    axes[0].set_ylabel('Class AP@50:95 advantage (pp)')
    axes[1].legend(loc='upper left',frameon=False,ncol=1)
    fig.tight_layout(pad=.7,w_pad=1.3);save(fig,'class_gaps_light')

    fig,ax=plt.subplots(figsize=(4.8,2.8))
    for i,model in enumerate(MODELS):
        q=gap_summary.loc[('full',model)].loc[DOMAINS]
        bars=ax.bar(np.arange(2)+(i-1)*.24,q['mean'],.24,yerr=q['std'],capsize=2,
                    color=COLORS[i],hatch=['','//','..'][i],edgecolor='white',label=model)
        ax.bar_label(bars,fmt='%.2f',padding=4,fontsize=7)
    ax.set_xticks(range(2),[f'{d} Test' for d in DOMAINS]);ax.set_ylim(0,57)
    ax.set_ylabel('Fixed-target mAP@50:95 advantage (pp)');ax.legend(frameon=False,ncol=3,loc='upper left')
    ax.set_axisbelow(True);ax.grid(axis='y',alpha=.18);fig.tight_layout();save(fig,'fixed_target_gaps_light')

    # Read only plain CSV members from the uploaded ZIPs; never deserialize weights.
    import zipfile,io,json
    curves={}
    for path in Path('/workspace/attachments').glob('*/RDD2022_V41_EXP_*.zip'):
        with zipfile.ZipFile(path) as z:
            identity=json.loads(z.read('run/run_identity.json'))
            model={'yolov8n.pt':'YOLOv8n','yolo11n.pt':'YOLO11n','yolo26n.pt':'YOLO26n'}[identity['train_configuration']['model']]
            domain=identity['train_domain'].removeprefix('China_');seed=identity['seed']
            f=pd.read_csv(io.BytesIO(z.read('run/results.csv')));f.columns=f.columns.str.strip()
            curves[(model,domain,seed)]=f
            dest=ROOT/'data/training_logs';dest.mkdir(exist_ok=True)
            f.to_csv(dest/f'{model}_{domain}_{seed}.csv',index=False)
    # The handoff also works without the original uploads: retained logs are sufficient.
    if not curves:
        for model in MODELS:
            for domain in DOMAINS:
                for seed in [13,37,71]:
                    curves[(model,domain,seed)]=pd.read_csv(ROOT/'data/training_logs'/f'{model}_{domain}_{seed}.csv')
    assert len(curves)==18
    fig,axes=plt.subplots(2,3,figsize=(7.16,4.35),sharex=True)
    for row,domain in enumerate(DOMAINS):
        for col,model in enumerate(MODELS):
            ax=axes[row,col]
            for seed,color,style in zip([13,37,71],COLORS,['-','--',':']):
                f=curves[(model,domain,seed)];peak=f.loc[f['metrics/mAP50-95(B)'].idxmax()]
                ax.plot(f.epoch,f['metrics/mAP50-95(B)']*100,label=f'Seed {seed}',color=color,lw=.9,ls=style)
                ax.plot(peak.epoch,peak['metrics/mAP50-95(B)']*100,'o',color=color,ms=3)
            ax.set_title(f'{model} / train {domain}',fontsize=8)
            ax.grid(alpha=.15);ax.set_xlim(1,150)
            if col==0:ax.set_ylabel('Source-val mAP (%)')
            if row==1:ax.set_xlabel('Epoch')
    axes[0,0].legend(frameon=False,fontsize=6,loc='lower right')
    fig.tight_layout(pad=.8,w_pad=.8,h_pad=1);save(fig,'validation_curves_light')
    print('Generated seven tables and four white-background PDF/PNG figures from verified metrics.')

if __name__=='__main__':
    main()
