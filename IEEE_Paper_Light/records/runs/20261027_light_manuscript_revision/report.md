# Revision report — 27/10/2026

Completed the authorized manuscript rewrite in a separate folder. The main paper includes three YOLO variants, correct target-fixed gaps and uncertainty, consistent training/test counts, balanced class findings, bounded claims and AI/data disclosures. Dark and duplicate/miscaptioned graphics are absent from the revised source package. Main PDF: 6 pages; supplement: 2 pages.

## Verification

- 72 raw metric rows, 18 runs, four-class mAP identity
- All saved means and sample SDs independently match raw metrics
- Fixed-target YOLO26 gap regression; all full and clean-only seed gaps positive
- Negative tests reject duplicate rows and missing fixed-target baselines
- 18 retained training CSVs have 150 epochs and the stated validation peaks
- main.pdf: 6 pages, resolved labels/citations, no missing glyphs or material horizontal overflow
- supplement.pdf: 2 pages, resolved labels/citations, no missing glyphs or material horizontal overflow
- Three distinct figure inclusions plus one optional plot; all four rendered backgrounds are white; no dark assets

Every page was rendered and inspected during layout work, including the revised supplementary tables/curves; no material horizontal clipping, missing glyph, unresolved reference or missing citation remains. IEEEtran initialization emits nonfatal XeLaTeX font-substitution warnings before fontspec activates the requested document fonts; visible text and Vietnamese names were checked.

## Editorial review perspectives (simulated self-review, not external peer review)

- Methodology/statistics: checked fixed-target estimand, gap SD, negative D40 findings, seed units and sensitivity population; causal and significance overclaims removed.
- Literature/contribution: added official YOLO26 documentation, removed unsupported novelty/SOTA and architecture-causality claims; unavailable full-text access recorded.
- Communication/layout: consolidated convergence discussion, rewrote abstract/conclusion to agree with results, supplied white figures only, placed detailed tables and all training curves in a compact supplement.

## Evidence limits and next action

No training, independent inference, original-image audit, scene-bootstrap or additional experiment was performed. Source scene/box audit statements remain author-reported and explicitly bounded. Authors should confirm affiliation, funding/conflicts/contributions and the target venue requirements before submission. Original uploaded manuscript and experiment archives remain unchanged.
