"""Generate the four agreed light figures from retained real metric/log CSVs.

All error bars are sample SD across the same three training seeds. Training
panels show each recorded seed, not synthetic or smoothed observations.
"""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/rdd-final-mpl')
import sys
import json
import subprocess
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
TOOLS=ROOT/'scripts/skill_tools'
sys.path.insert(0,str(TOOLS))
from audit_panel_alignment import require_matplotlib_panel_alignment

MODELS=['YOLO11n','YOLOv8n','YOLO26n']
DOMAINS=['Drone','MotorBike']
SEEDS=[13,37,71]
COLORS=['#397EAD','#D4892C','#27816B']

def export(fig,stem):
    if len(sys.argv)>1 and stem not in sys.argv[1:]:
        plt.close(fig)
        return
    fig.canvas.draw()
    require_matplotlib_panel_alignment(fig,json_out=ROOT/f'qa/figures/{stem}.alignment.json',
        overlay_svg=ROOT/f'qa/figures/{stem}.alignment.svg',tolerance_pt=1.5,gutter_tolerance_pt=1.5,strict=True)
    fig.savefig(ROOT/f'figures/{stem}.pdf',facecolor='white')
    fig.savefig(ROOT/f'figures/{stem}.svg',facecolor='white')
    fig.savefig(ROOT/f'figures/{stem}.png',facecolor='white',dpi=600)
    fig.savefig(ROOT/f'figures/{stem}.tiff',facecolor='white',dpi=600,
                pil_kwargs={'compression':'tiff_lzw'})
    plt.close(fig)
    audits=[
        [sys.executable,str(TOOLS/'audit_pdf_text.py'),str(ROOT/f'figures/{stem}.pdf'),'--min-pt','5'],
        [sys.executable,str(TOOLS/'audit_figure_collisions.py'),str(ROOT/f'figures/{stem}.pdf'),
         '--json-out',str(ROOT/f'qa/figures/{stem}.collision.json'),
         '--overlay-pdf',str(ROOT/f'qa/figures/{stem}.collision-overlay.pdf')]
    ]
    for i,cmd in enumerate(audits):
        p=subprocess.run(cmd,capture_output=True,text=True)
        (ROOT/f'qa/figures/{stem}.audit{i+1}.txt').write_text(p.stdout+p.stderr)
        print(stem,['text','collision'][i], 'exit',p.returncode,p.stdout.strip()[-650:])
        if p.returncode:raise RuntimeError(f'{stem} rendered QA failed: exit {p.returncode}; see qa/figures')

def main():
    plt.style.use('default')
    plt.rcParams.update({'font.family':'sans-serif','font.sans-serif':['DejaVu Sans'],'font.size':8,'axes.titlesize':8.5,
        'axes.labelsize':8,'xtick.labelsize':7.5,'ytick.labelsize':7.5,'legend.fontsize':7.2,
        'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white',
        'axes.spines.top':False,'axes.spines.right':False,'axes.linewidth':.7,
        'pdf.fonttype':42,'ps.fonttype':42,'svg.fonttype':'none'})
    source=pd.read_csv(ROOT/'data/all_metrics.csv')
    full=source[source.subset=='full']
    if full.duplicated(['model','train','target','seed']).any():raise ValueError('Duplicate metric rows')
    assert len(full)==36
    # Establish gap pairing from raw records, rather than trusting displayed summaries.
    paired=[]
    for model in MODELS:
        for target in DOMAINS:
            a=full[(full.model==model)&(full.train==target)&(full.target==target)].set_index('seed')
            b=full[(full.model==model)&(full.train!=target)&(full.target==target)].set_index('seed')
            assert len(a)==len(b)==3
            for seed in SEEDS:
                row=dict(model=model,target=target,seed=seed,gap=(a.loc[seed,'map50_95']-b.loc[seed,'map50_95'])*100)
                for cls in ['D00','D10','D20','D40']:
                    row[cls]=(a.loc[seed,cls+'_ap50_95']-b.loc[seed,cls+'_ap50_95'])*100
                paired.append(row)
    paired=pd.DataFrame(paired)
    paired.to_csv(ROOT/'qa/figures/plot_source_gaps.csv',index=False)
    full.to_csv(ROOT/'qa/figures/plot_source_scores.csv',index=False)

    fig,axes=plt.subplots(1,3,figsize=(7.16,2.4))
    for seed,color,style in zip(SEEDS,COLORS,['-','--',':']):
        f=pd.read_csv(ROOT/f'data/training_logs/YOLO11n_Drone_{seed}.csv')
        assert f.epoch.tolist()==list(range(1,151))
        train=f[[c for c in f if c.startswith('train/') and c.endswith('_loss')]].sum(axis=1)
        val=f[[c for c in f if c.startswith('val/') and c.endswith('_loss')]].sum(axis=1)
        ap=f['metrics/mAP50-95(B)']*100
        for ax,y in zip(axes,[train,val,ap]):ax.plot(f.epoch,y,color=color,ls=style,lw=.9,label=f'Seed {seed}')
        peak=ap.idxmax();axes[2].plot(f.loc[peak,'epoch'],ap.loc[peak],'o',ms=3,color=color)
    for ax,title,ylabel in zip(axes,['Training loss','Validation loss','Validation mAP@50:95'],['Logged loss sum','Logged loss sum','mAP@50:95 (%)']):
        ax.set_title(title);ax.set_xlabel('Epoch');ax.set_ylabel(ylabel);ax.set_xlim(1,150);ax.grid(alpha=.15)
    fig.legend(*axes[0].get_legend_handles_labels(),ncol=3,frameon=False,loc='upper center',bbox_to_anchor=(.5,.99))
    fig.subplots_adjust(left=.075,right=.985,bottom=.22,top=.74,wspace=.49)
    export(fig,'training_curves')

    fig,ax=plt.subplots(figsize=(3.5,2.8))
    for i,model in enumerate(MODELS):
        q=paired[paired.model==model].groupby('target').gap.agg(['mean','std']).loc[DOMAINS]
        xs=np.arange(2)+(i-1)*.24
        ax.bar(xs,q['mean'],.24,yerr=q['std'],capsize=2,color=COLORS[i],edgecolor='white',linewidth=.4,label=model)
        for x,mean,sd in zip(xs,q['mean'],q['std']):ax.text(x,mean+sd+1.3,f'{mean:.2f}',ha='center',va='bottom',fontsize=7)
    ax.set_xticks(range(2),[f'{d} Test' for d in DOMAINS]);ax.set_ylim(0,57)
    ax.set_ylabel('Fixed-target mAP@50:95 gap (pp)');ax.grid(False)
    fig.legend(*ax.get_legend_handles_labels(),loc='upper center',ncol=3,frameon=False,bbox_to_anchor=(.52,.99),columnspacing=.8,handlelength=1.2)
    fig.subplots_adjust(left=.18,right=.98,bottom=.17,top=.84)
    export(fig,'paired_gaps_comparison')

    fig,ax=plt.subplots(figsize=(3.5,2.8))
    for i,model in enumerate(MODELS):
        q=paired[(paired.model==model)&(paired.target=='MotorBike')]
        means=[q[c].mean() for c in ['D00','D10','D20','D40']]
        sds=[q[c].std(ddof=1) for c in ['D00','D10','D20','D40']]
        ax.bar(np.arange(4)+(i-1)*.24,means,.24,yerr=sds,capsize=1.7,color=COLORS[i],edgecolor='white',linewidth=.4,label=model)
    ax.set_xticks(range(4),['D00','D10','D20','D40']);ax.set_ylim(0,70)
    ax.set_xlabel('Damage class');ax.set_ylabel('Fixed-target class AP advantage (pp)')
    ax.grid(axis='y',alpha=.16);ax.set_axisbelow(True)
    fig.legend(*ax.get_legend_handles_labels(),loc='upper center',ncol=3,frameon=False,bbox_to_anchor=(.52,.99),columnspacing=.8,handlelength=1.2)
    fig.subplots_adjust(left=.18,right=.98,bottom=.20,top=.84)
    export(fig,'class_gap_motorbike')

    fig,axes=plt.subplots(1,2,figsize=(7.16,2.9),sharey=True)
    for ax,target,letter in zip(axes,DOMAINS,['a','b']):
        for i,is_target in enumerate([True,False]):
            means=[];sds=[]
            for model in MODELS:
                q=full[(full.model==model)&(full.target==target)&((full.train==target) if is_target else (full.train!=target))]
                means.append(q.map50_95.mean()*100);sds.append(q.map50_95.std(ddof=1)*100)
            xs=np.arange(3)+(i-.5)*.34
            ax.bar(xs,means,.34,yerr=sds,capsize=2,color=[COLORS[0],COLORS[1]][i],edgecolor='white',linewidth=.4,label=['Target-domain training','Other-domain training'][i])
            for x,mean,sd in zip(xs,means,sds):ax.text(x,mean+sd+1.2,f'{mean:.2f}',ha='center',va='bottom',fontsize=7)
        ax.set_xticks(range(3),MODELS);ax.set_ylim(0,68);ax.set_title(f'{target} Test');ax.grid(False)
        ax.text(-.07,1.04,letter,transform=ax.transAxes,fontweight='bold',fontsize=9)
    axes[0].set_ylabel('mAP@50:95 (%)')
    fig.legend(*axes[0].get_legend_handles_labels(),loc='upper center',ncol=2,frameon=False,bbox_to_anchor=(.52,.99))
    fig.subplots_adjust(left=.075,right=.985,bottom=.17,top=.80,wspace=.17)
    export(fig,'domain_comparison')
    (ROOT/'qa/figures/data_contract.json').write_text(json.dumps({
        'backend':'Python/matplotlib','subset':'full','metric_rows':36,'gap_rows':18,'seeds':SEEDS,
        'center':'arithmetic mean','uncertainty':'sample SD, ddof=1','pairing':'same model, target, seed; change training domain',
        'training_figure':'original representative YOLO11n Drone experiment; all150epochs x3seeds',
        'class_figure_target':'MotorBike; Drone class results remain in the main class-AP table',
        'exclusions':'No metric observations excluded within declared full-test figures; clean-only is a separately reported sensitivity subset',
        'figure_roles':{'training_curves':'training trajectory support','paired_gaps_comparison':'fixed-target gap magnitude and target asymmetry','class_gap_motorbike':'class-specific transfer vulnerability','domain_comparison':'new-model in-domain gains versus remaining cross-domain deficit'}},indent=2))
    print('All four light figures generated with alignment, glyph and collision audits.')

if __name__=='__main__':main()
