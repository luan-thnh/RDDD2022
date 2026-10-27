"""Apply scoped, traceable YOLO26 integration to the author's pre-YOLO26 source.

Only writes this manuscript's main.tex, references.bib and change records.
Metric summaries were verified against the uploaded archive CSV/JSON records.
"""
from pathlib import Path
import csv
import difflib
import json
import re
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'provenance/before_yolo26'
MODELS=['YOLO11n','YOLOv8n','YOLO26n']
DOMAINS=['Drone','MotorBike']

def main():
    original=(BASE/'main.tex').read_text()
    text=original
    changes=[]
    def edit(old,new,reason,anchor):
        nonlocal text
        if text.count(old)!=1:raise ValueError(f'Expected one match for {anchor}; found {text.count(old)}')
        text=text.replace(old,new,1)
        changes.append(dict(anchor=anchor,reason=reason,before=old,after=new))
    def para(prefix):
        hits=re.findall('^'+re.escape(prefix)+'.*$',text,re.M)
        if len(hits)!=1:raise ValueError(prefix)
        return hits[0]
    def table(label,rows,header=None):
        nonlocal text
        chunks=list(re.finditer(r'\\begin\{table\*?\}.*?\\end\{table\*?\}',text,re.S))
        hit=next(m for m in chunks if r'\label{'+label+'}' in m.group())
        block=hit.group()
        start=block.index(r'\midrule')+len(r'\midrule')
        end=block.index(r'\bottomrule',start)
        new=block[:start]+'\n'+'\n'.join(' & '.join(map(str,r))+r' \\' for r in rows)+'\n'+block[end:]
        if header:new=new.replace(header[0],header[1])
        if label=='tab:map50':new=new.replace(r'\begin{tabular}',r'\small\setlength{\tabcolsep}{4pt}'+'\n'+r'\begin{tabular}',1)
        edit(block,new,'Add YOLO26 and use recomputed means/sample SDs; preserve table in main.',label)
    def pm(a,b):return f'${a:.2f}\\pm{b:.2f}$'

    edit('% Font packages removed - using IEEEtran default Times font for pdfLaTeX compatibility',
         '% !TEX program = xelatex\n% Unicode-safe, Times-compatible fonts for the original IEEEtran layout.\n'+
         '\\usepackage{fontspec}\n\\setmainfont{Liberation Serif}[SmallCapsFont={Latin Modern Roman Caps}]\n\\setsansfont{Liberation Sans}\n\\setmonofont{Liberation Mono}[Scale=MatchLowercase]',
         'Resolve the Unicode author-name problem recorded in the conversation.','toolchain-fonts')
    edit('\\usepackage[backend=biber,style=ieee,sorting=none,giveninits=true,maxbibnames=6,doi=true,url=true]{biblatex}\n\\addbibresource{references.bib}',
         '\\usepackage{cite}\n\\usepackage[hidelinks]{hyperref}',
         'Use available BibTeX tooling; preserve all original citation keys.','toolchain-bibliography')
    edit('\\usepackage{siunitx}\n\\sisetup{detect-all}\n','', 'Remove unused package dependency; no scientific text or units change.','unused-siunitx')
    old=para('Road-damage detectors')
    new=r'''Road-damage detectors are often evaluated on imagery resembling their training data, yet deployment across camera platforms can reduce accuracy. This study quantifies the magnitude, asymmetry, and class dependence of cross-domain transfer between the China\_Drone and China\_MotorBike subsets of RDD2022. We use a scene-aware split and compare target-domain-trained and other-domain-trained detectors on identical held-out target images. The locked subset contains 4,378 images, including 658 test images, and four damage classes. COCO-pretrained YOLO11n, YOLOv8n, and YOLO26n are independently fine-tuned on each domain with three matched seeds and 150 epochs per run (18 runs). Mean fixed-target mAP@50:95 gaps range from 14.86 to 16.91 percentage points on Drone Test and from 41.24 to 42.94 points on MotorBike Test. For YOLO26n, the respective gaps are $16.91\pm0.80$ and $42.27\pm1.28$ points, where uncertainty is sample standard deviation over three seeds. All 18 seed-specific comparisons favor target-domain training. On MotorBike Test, D20 relative class-AP declines range from 96.14\% to 98.30\% against the target-trained baselines. YOLO26n improves mean in-domain mAP over YOLOv8n by 3.08 and 3.50 points on Drone and MotorBike, respectively, while substantial gaps persist. The study contributes a reproducible bidirectional protocol and a three-variant replication of domain-associated asymmetry and class-specific vulnerability. Acquisition geometry, training size, and other collection differences remain jointly varying factors.'''
    edit(old,new,'Complete the agreed concise Objective–Methods–Results–Contribution abstract with correct three-model evidence.','abstract')
    edit('RDD2022, YOLO11n, YOLOv8n, scene-aware','RDD2022, YOLO11n, YOLOv8n, YOLO26n, scene-aware','Add the third evaluated model.','keywords')
    old=para('We address three research questions:')
    new=r'''We address four research questions: \textbf{RQ1}: How large and asymmetric are the fixed-target performance gaps? \textbf{RQ2}: Are gap directions and magnitudes consistent across random seeds and the three tested YOLO variants? \textbf{RQ3}: How does transfer vary among D00, D10, D20, and D40? \textbf{RQ4}: Does the addition of YOLO26n improve absolute accuracy while reducing or preserving domain-gap magnitude? \textbf{Our contributions are}: (1) a reproducible bidirectional evaluation with scene-aware partitions and fixed target test sets; (2) seed-resolved evidence of target asymmetry and class-specific vulnerability; and (3) replication across YOLO11n, YOLOv8n, and YOLO26n under matched explicit fine-tuning settings. The study provides a descriptive evaluation of source-domain choice rather than a new detector or an isolated causal estimate of viewpoint effects.'''
    edit(old,new,'Complete the four-RQ and explicit contribution updates already introduced in the conversation.','introduction-RQs')
    old=para(r'\textbf{Consensus:')
    new=old.replace('object detectors trained on one visual distribution','learned predictors trained on one visual distribution')
    new=new.replace('large benchmarks such as WILDS \\cite{koh2021wilds} and COCO \\cite{lin2014coco} illustrate','benchmarks such as WILDS \\cite{koh2021wilds} illustrate')
    new=new.replace('smartphone-image classification','smartphone-image detection and classification').replace('implicitly acknowledging that camera platform matters','providing a setting in which camera-platform transfer can be examined')
    edit(old,new,'Keep Consensus paragraph; remove the misplaced use of COCO as a shift benchmark.','related-consensus')
    old=para(r'\textbf{Trade-off:')
    new=old.replace('holds the detector and training protocol fixed while systematically varying only the source acquisition domain, trading adaptation gains for clearer causal attribution of performance differences to domain choice.',
                    'holds each detector\'s explicit fine-tuning settings fixed while varying the source acquisition domain, prioritizing a clear measurement of domain-associated performance differences.')
    evolution=r'''\textbf{YOLO family evolution.} YOLOv8 \cite{ultralyticsyolov8}, YOLO11 \cite{jocher2024yolo11}, and YOLO26 \cite{ultralyticsyolo26} provide related compact detector variants with different pretrained checkpoints and model-specific implementations. Repeating the same fixed-target protocol across them tests whether the observed gap is confined to one variant. Matched explicit fine-tuning settings improve comparability, while architecture, pretraining, and implementation differences remain coupled.'''
    edit(old,new+'\n\n'+evolution,'Retain Trade-off paragraph and add the YOLO-evolution paragraph requested in the ongoing edit; remove causal attribution claim.','related-tradeoff-evolution')
    old=para(r'\textbf{Gap:')
    new=r'''\textbf{Gap: bidirectional asymmetry and class-level vulnerability.} Comparing one model on two different test sets conflates transfer behavior with intrinsic test-set difficulty. A fixed-target comparison is needed to quantify the advantage of target-domain training on each acquisition domain and to determine how that contrast varies across D00, D10, D20, and D40. The question addressed here is how large these two target-specific gaps are, whether their direction recurs across seeds and models, and which classes depart from the aggregate pattern.'''
    edit(old,new,'Preserve the research-gap role while removing an unverified universal no-prior-study assertion.','related-gap')
    old=para(r'\textbf{This paper.}')
    new=old.replace('COCO-pretrained YOLO11n','COCO-pretrained \\cite{lin2014coco} YOLO11n')
    new=new.replace('and YOLOv8n \\cite{ultralyticsyolov8}', 'YOLOv8n \\cite{ultralyticsyolov8}, and YOLO26n \\cite{ultralyticsyolo26}')
    new=new.replace('YOLO11n \\cite{jocher2024yolo11}, YOLOv8n','YOLO11n \\cite{jocher2024yolo11}, YOLOv8n')
    # The original has no comma before "and"; normalize this local list only.
    new=new.replace('YOLO11n \\cite{jocher2024yolo11} YOLOv8n','YOLO11n \\cite{jocher2024yolo11}, YOLOv8n')
    new=new.replace('two independently trained compact detector families','three independently fine-tuned compact YOLO variants')
    new=new.replace('descriptive two-architecture replication that isolates asymmetry magnitude','descriptive three-variant replication that measures asymmetry magnitude')
    edit(old,new,'Extend the original positioning paragraph and restore COCO citation to its proper pretraining role.','related-this-paper')
    edit('We use the China\\_Drone (2,401 images) and China\\_MotorBike (1,977 images) subsets from RDD2022.',
         'We use the China\\_Drone (2,401 images) and China\\_MotorBike (1,977 images) subsets from the publicly released RDD2022 dataset \\cite{arya2024rdd2022}. The train/validation/test partitions below are the derived v4.1 partitions used in this study.',
         'Address the earlier request to state the public dataset source and distinguish the derived partition.','dataset-source')
    edit(r'\texttt{yolo11n.pt} or \texttt{yolov8n.pt}',r'\texttt{yolo11n.pt}, \texttt{yolov8n.pt}, or \texttt{yolo26n.pt}', 'Add verified initial checkpoint.','training-model')
    edit('$2\\times2\\times3=12$ runs','$3\\times2\\times3=18$ runs','Update experimental run count.','training-count')
    edit('mAP@50:95 of architecture $m$','mAP@50:95 in percentage units of model $m$','Clarify units for pp subtraction without changing the equation.','metric-units')

    summary=pd.read_csv(ROOT/'data/metric_summary.csv');full=summary[summary.subset=='full']
    gaps=pd.read_csv(ROOT/'data/gap_summary.csv');gaps=gaps[gaps.subset=='full']
    seedg=pd.read_csv(ROOT/'data/fixed_target_gaps_by_seed.csv');seedg=seedg[seedg.subset=='full']
    rows=[]
    for model in MODELS:
        for i,train in enumerate(DOMAINS):
            q=full[(full.model==model)&(full.train==train)].set_index('target')
            cells=[pm(q.loc[t,'map50_95_mean'],q.loc[t,'map50_95_sd']) for t in DOMAINS]
            rows.append([r'\multirow{2}{*}{'+model+'}' if i==0 else '',train,*cells,3])
    table('tab:matrix',rows)
    rows=[]
    for model in MODELS:
        for train in DOMAINS:
            q=full[(full.model==model)&(full.train==train)].set_index('target')
            rows.append([model,train,*[pm(q.loc[t,'map50_mean'],q.loc[t,'map50_sd']) for t in DOMAINS]])
    table('tab:map50',rows)
    rows=[]
    for model in MODELS:
        q=gaps[gaps.model==model].set_index('target')
        rows.append([model,*[pm(q.loc[t,'mean'],q.loc[t,'std']) for t in DOMAINS]])
    table('tab:paired',rows)
    rows=[]
    for model in MODELS:
        for target in DOMAINS:
            q=seedg[(seedg.model==model)&(seedg.target==target)].set_index('seed')
            rows.append([model,target,*[f'{q.loc[s,"gap_pp"]:.2f}' for s in [13,37,71]]])
    table('tab:seeds',rows)
    edit('All 12 values are positive.','All 18 values are positive.','Update seed-specific paired comparison count.','seed-caption')
    rows=[]
    for target in DOMAINS:
        for model in MODELS:
            for train in DOMAINS:
                q=full[(full.model==model)&(full.train==train)&(full.target==target)].iloc[0]
                rows.append([model,train,target,*[f'{q[c+"_ap50_95_mean"]:.2f}' for c in ['D00','D10','D20','D40']]])
    table('tab:classap',rows)
    old=para('Table~\\ref{tab:matrix} contains')
    new=old.replace('Both architectures','All three models')
    new=new.replace('This supports a strong, asymmetric', 'YOLO26n adds corresponding gaps of $16.91\\pm0.80$ and $42.27\\pm1.28$~pp. This supports a strong, asymmetric')
    edit(old,new,'Append the new model result to the original RQ1 account.','results-RQ1')
    old=para('Figure~\\ref{fig:training} presents')
    new=r'''Figure~\ref{fig:training} presents the original representative training and validation trajectories for YOLO11n trained on Drone across three random seeds. Training loss declined steadily, while validation loss fluctuated before stabilizing. Maximum logged validation mAP@50:95 occurred at epochs 110, 92, and 111 for seeds 13, 37, and 71, respectively. Across the full experiment, all 18 runs completed 150 epochs with patience set to zero; the maximum logged validation-mAP epochs ranged from 63 to 133. The histories support completed, stable training under the stated budget. A pre-final-epoch validation peak does not establish global convergence or an optimal schedule, and maximum logged mAP alone does not independently verify the fitness rule used to save \texttt{best.pt}.'''
    edit(old,new,'Retain convergence analysis and its original representative experiment; correct early-stopping/epoch/variance claims.','results-training')
    edit('Training and validation metrics for YOLO11n across three seeds. Top row: loss trajectories. Bottom row: mAP@50:95 progression. Shaded regions indicate inter-seed variation. Best validation checkpoints (marked with circles) were saved between epochs 92--111.',
         'Training and validation metrics for YOLO11n trained on Drone across seeds 13, 37, and 71. Left to right: summed logged training-loss components, summed logged validation-loss components, and validation mAP@50:95. Circles mark maximum logged mAP at epochs 110, 92, and 111; individual seed trajectories are shown without a shaded uncertainty band.',
         'Make the original caption match the actual light three-panel training figure.','training-caption')
    old=para('For YOLO11n, paired gaps')
    new=old.replace('The gap \\emph{direction}', 'YOLO26n adds Drone-target gaps of 16.91, 16.10, and 17.71~pp and MotorBike-target gaps of 43.14, 42.87, and 40.80~pp. The gap \\emph{direction}')
    new=new.replace('across both architectures','across all three variants and all 18 model--target--seed comparisons')
    new=new.replace('Two model families are insufficient to claim architecture-independent generalization, and the comparison does not isolate architectural changes from the associated training recipes.', 'The three reused seed values and three variants from one model family support within-family replication; architectural changes remain coupled with pretraining and model-specific implementation differences.')
    edit(old,new,'Append verified YOLO26 seed gaps; preserve the original seed-resolved evidence in main.','results-RQ2')
    old=para('Figure~\\ref{fig:classes} compares')
    new=old.replace('both detector families','all three variants')
    edit(old,new,'Extend class analysis while retaining the original sparse-D40 discussion.','results-RQ3-a')
    old=para('Table~\\ref{tab:classap} makes')
    new=old.replace('\\emph{both} architectures','\\emph{all three} models')
    new=new.replace('each family, whereas','each model (57.72, 53.21, and 56.45~pp for YOLO11n, YOLOv8n, and YOLO26n), whereas')
    new=new.replace('can exhibit a small or negative fixed-target advantage because its support is sparse', 'shows negative mean fixed-target advantages ($-6.61$, $-9.74$, and $-1.95$~pp, respectively) with sparse support')
    edit(old,new,'Use the measured class contrasts without inventing a causal mechanism.','results-RQ3-b')
    marker=r'\subsection{Evaluation Sensitivity and Convergence}'
    extension=r'''\subsection{RQ4: Multi-Architecture Comparison}
Figure~\ref{fig:domain} compares all three variants on each fixed target. YOLO26n achieves the highest mean in-domain mAP@50:95: 24.49\% on Drone Test and 54.75\% on MotorBike Test. These exceed YOLOv8n by 3.08 and 3.50~pp, corresponding to relative gains of 14.38\% and 6.83\%. Its fixed-target gaps nevertheless remain 16.91 and 42.27~pp. Dividing each gap by the mean target-trained score on that same target gives relative declines of 69.04\% and 77.20\%. Thus, the additional model strengthens the original finding: higher in-domain mean accuracy does not eliminate the cross-domain deficit.

The effect is not a uniform ranking across classes or targets. YOLO11n retains higher in-domain D20 AP on MotorBike Test than YOLO26n (58.72\% versus 57.99\%). YOLO26n's MotorBike-target gap is slightly below YOLO11n's, while its Drone-target gap is larger. These three-seed comparisons do not establish the statistical significance of between-model differences.

\begin{figure*}[t]
\centering\includegraphics[width=\textwidth]{figures/domain_comparison.pdf}
\caption{Three-model comparison grouped by fixed target. Within each panel, target-domain-trained and other-domain-trained models are tested on identical held-out images. Bars show mean mAP@50:95 and error bars sample SD over seeds 13, 37, and 71. YOLO26n has higher in-domain mean scores while substantial target-specific gaps remain.}\label{fig:domain}
\end{figure*}

'''
    edit(marker,extension+marker,'Complete the existing RQ4 and domain-comparison-figure integration from the conversation; add no duplicate training figure.','results-RQ4')
    old=para('All 12 training histories')
    new=old.replace('All 12','All 18')
    new=new.replace('Clean-only evaluations preserve the main direction of the target-trained advantage;', 'Clean-only evaluations preserve the positive target-trained advantage in all 18 comparisons, with mean Drone/MotorBike gaps of 14.93/43.86~pp for YOLO11n, 15.25/41.87~pp for YOLOv8n, and 16.59/42.60~pp for YOLO26n;')
    edit(old,new,'Update the original sensitivity paragraph with the verified third-model result.','results-sensitivity')
    edit(r'\section{Discussion and Threats to Validity}',r'\section{Discussion}', 'Follow the conversation\'s explicit Discussion/Limitations/Threats organization.','discussion-heading')
    old=para('The same-target design removes')
    new=old.replace('across both compact architectures and all seeds','across all three compact YOLO variants and all seed-specific comparisons')
    edit(old,new,'Extend the original central interpretation without replacing its role.','discussion-central')
    old=para(r'\textbf{Why does performance degrade?}')
    new=r'''\textbf{Why does performance degrade?} Three factors provide hypotheses for interpreting the observed domain gap. First, \textbf{scale mismatch}: overhead and near-ground imagery can present defects at different pixel scales and perspectives, potentially changing the visual information available to a detector. Object-scale distributions and paired views were not measured here, so a scale mechanism remains to be tested. Second, \textbf{context distribution shift}: different roadway framing and surrounding backgrounds may alter source-domain cues. The fixed-target contrast shows that source choice matters but does not distinguish context from illumination, road-surface differences, or annotation density. Third, \textbf{class-specific fragility}: on MotorBike Test, D20 AP falls from 58.72\% to 1.00\% for YOLO11n, from 55.35\% to 2.14\% for YOLOv8n, and from 57.99\% to 1.54\% for YOLO26n when target-domain training is replaced by Drone training. Relative to the target-trained class means, these declines are 98.30\%, 96.14\%, and 97.34\%; D00 declines on the same target are smaller at 56.57\%, 56.37\%, and 51.88\%. Fine-texture and scale sensitivity are plausible explanations for this class contrast, requiring controlled or per-image analysis to establish their roles.'''
    edit(old,new,'Keep the original three-factor discussion and correct its evidence level and fixed-target class numbers.','discussion-factors')
    old=para(r'\textbf{Comparison with prior work.}')
    new=r'''\textbf{Comparison with prior work.} Our findings support the motivation for distribution-aware evaluation in domain-generalization research and WILDS \cite{zhou2023survey,koh2021wilds}, while focusing on two road-acquisition domains and their class-specific contrasts. The fixed-target protocol complements detector-enhancement work such as YOLO-RD \cite{wang2025yolord}; we do not numerically rank studies with incompatible partitions and label policies. COCO \cite{lin2014coco} supplies the pretraining context rather than evidence of adaptation on these road datasets. The MotorBike-target advantage exceeds the Drone-target advantage by 27.80, 26.38, and 25.36~pp for YOLO11n, YOLOv8n, and YOLO26n, respectively. This quantifies the difference between two target-specific gaps without establishing that either acquisition platform intrinsically produces more transferable features.'''
    edit(old,new,'Retain prior-work comparison; fix misplaced COCO citation and 12.24-pp asymmetry interpretation.','discussion-prior-work')
    old=para('Several limitations remain.')
    new=r'''\subsection{Limitations}
Several design choices bound the interpretation. Training sizes differ (1,680 versus 1,383 images), and acquisition domain can also vary with location, roadway condition, illumination, and annotation density. No balancing or ablation study separates these factors. Three seed values and three compact variants from one YOLO family support replication on the fixed datasets, not precise population-level inference or architecture-independent generalization. Both domains are China subsets, so transfer to other countries and devices remains unmeasured. D40 has sparse Drone support, and filtered classes outside D00--D40 are not ignore regions. These constraints motivate targeted controls rather than treating the observed gaps as isolated viewpoint effects.

\subsection{Threats to Validity}
The scene-review and conservative grouping address identified similarity candidates but cannot guarantee that all latent scene overlap was found. Some MotorBike images were encountered during exploratory analysis before split finalization, limiting an entirely untouched-holdout claim. Clean-only evaluation retains the gap direction but changes the image population. The present analysis checks and recomputes archived metric summaries; it does not independently rerun inference from each checkpoint on every original test image or replay the original image/XML audit. Seed SDs are descriptive and do not replace scene-level uncertainty estimates.'''
    edit(old,new,'Complete the already-planned Limitations/Threats split while retaining each material boundary once.','discussion-limitations-threats')
    edit('present 12-run result','present 18-run result','Update the original future-control paragraph.','discussion-run-count')
    old=para('These restrictions are relevant')
    edit(old,'The study establishes a seed-resolved, descriptive replication of domain-associated gaps on the locked partition. The next controls should test the source-size, scene-composition, and acquisition-geometry explanations identified above.',
         'Apply claim-forward guidance: retain boundaries in named sections and close with the supported contribution and next test.','discussion-close')
    old=para('On the scene-reviewed RDD2022')
    new=r'''On the scene-reviewed RDD2022 v4.1 Drone/MotorBike split, 18 fine-tuning runs across YOLO11n, YOLOv8n, and YOLO26n show consistent in-domain advantages under fixed-target evaluation. Mean gaps range from 14.86 to 16.91~pp on Drone Test and from 41.24 to 42.94~pp on MotorBike Test, with distinct class-level behavior. \textbf{Key quantitative findings:} (1) all 18 full-test seed comparisons and their clean-only counterparts favor target-domain training; (2) MotorBike-target D20 relative AP declines range from 96.14\% to 98.30\% against the target-trained baselines, while sparse Drone-target D40 shows negative mean class gaps; and (3) MotorBike-target advantages exceed Drone-target advantages by 25.36--27.80~pp across the three variants. YOLO26n raises in-domain mean accuracy while preserving the substantial cross-domain gap.'''
    edit(old,new,'Close the four RQs with the verified three-model evidence, retaining the original conclusion format.','conclusion-results')
    old=para(r'\textbf{Practical implications:}')
    new=old.replace('substantial performance loss—potentially halving detection rates—','substantial mAP degradation and validate performance on the intended target platform; they should ')
    new=new.replace('should budget for substantial mAP degradation and validate performance on the intended target platform; they should and prioritize','should budget for substantial mAP degradation, validate performance on the intended target platform, and prioritize')
    new=new.replace('Fine-textured damage classes (alligator cracks) require particular attention under cross-domain conditions.', 'Class-level validation is important because aggregate mAP can hide large D20 losses and sparse-class reversals.')
    edit(old,new,'Keep practical implications and future-work flow; remove the unsupported equivalence between mAP and detection rate.','conclusion-implications')
    old=para('The source RDD2022 dataset is cited')
    new=old.replace('The scene review was AI-assisted and independently checked by the researcher.', 'The recorded scene review was AI-assisted and checked by the researcher; manuscript editing and figure preparation also used AI assistance.')
    edit(old,new,'Retain author-supplied provenance and declaration boundary; disclose the actual editing assistance.','declarations')
    edit(r'\printbibliography',r'\balance'+'\n'+r'\bibliographystyle{ieeetr}'+'\n'+r'\bibliography{references}', 'Complete the supported local bibliography toolchain.','bibliography-output')

    # Small semantic polish from the abstract/triad review: keep the same facts,
    # but make the background contrast, objective and contribution explicit.
    text=text.replace('Road-damage detectors are often evaluated on imagery resembling their training data, yet deployment across camera platforms can reduce accuracy.',
        'Road-damage detectors are often evaluated on imagery resembling their training data; however, deployment across camera platforms can reduce accuracy.',1)
    text=text.replace('This study quantifies the magnitude, asymmetry, and class dependence',
        'This study aims to quantify the magnitude, asymmetry, and class dependence',1)
    text=text.replace('The study contributes a reproducible bidirectional protocol and a three-variant replication',
        'Our contribution is a reproducible bidirectional protocol and a three-variant replication',1)
    final_claim='YOLO26n raises in-domain mean accuracy while preserving the substantial cross-domain gap.'
    text=text.replace(final_claim,final_claim+' The contribution is a seed-resolved, three-variant comparison of source-domain choice on fixed target test sets.',1)
    changes.append(dict(anchor='skill-semantic-polish',reason='Make the already-supported background, objective and contribution explicit; retain all results and evidence boundaries.',before='Equivalent background/objective/contribution wording',after='Explicit five-element abstract and aligned conclusion contribution'))
    (ROOT/'main.tex').write_text(text)
    bib=(BASE/'references.bib').read_text()
    bib+=r'''
@misc{ultralyticsyolo26,
  author={{Ultralytics}}, title={{YOLO26} Model Documentation}, year={2026},
  howpublished={\url{https://docs.ultralytics.com/models/yolo26/}},
  note={Accessed 27 October 2026}
}
'''
    (ROOT/'references.bib').write_text(bib)
    (ROOT/'qa/integration_changes.json').write_text(json.dumps(changes,indent=2,ensure_ascii=False))
    (ROOT/'qa/baseline_to_final.diff').write_text(''.join(difflib.unified_diff(original.splitlines(True),text.splitlines(True),fromfile='before_yolo26/main.tex',tofile='final/main.tex')))
    with (ROOT/'qa/integration_map.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['anchor','change_reason']);w.writerows((x['anchor'],x['reason']) for x in changes)
    (ROOT/'qa/rewrite_contracts.tex').write_text('\n\n'.join(
        '% [LLM] '+x['anchor']+'\n% Changed: '+x['reason']+
        '\n% Protected: original citation keys, labels and equation structures retained; verified metric values changed only where listed.'+
        '\n% Meaning-Check: NEEDS-LLM' +
        '\n% Risk-Flags: '+('not-assessed' if x['anchor'].startswith('toolchain') else 'terminology-drift') for x in changes))
    print(f'Applied {len(changes)} scoped edits to the actual pre-YOLO26 source; diff and change map saved.')

if __name__=='__main__':main()
