# Chart verification

verify-charts: 13_performance.svg | object=drone-performance | type=horizontal-bar+SD | mode=decomposable-calc | scale=0-60 from ticks | calc=ran | six widths match CSV means within 0.001 px; whiskers match mean ± sample SD; y is ordinal category spacing.
verify-charts: 13_performance.svg | object=motorbike-performance | type=horizontal-bar+SD | mode=decomposable-calc | scale=0-60 from ticks | calc=ran | six widths match CSV means within 0.001 px; SD preserved; same scale as Drone panel.
verify-charts: 14_seed_gap.svg | object=seed-gap | type=scatter+range | mode=decomposable-calc | scale=0-50 from ticks | calc=ran×6 | x=330+15×gap; all 18 x positions match within 0.001 px; ±3px y jitter distinguishes seeds, not a quantitative measure; connector=min–max, not CI.
verify-charts: 15_class_gap.svg | object=class-gap | type=grouped-column | mode=decomposable-calc | scale=0-60 from ticks | calc=ran×3 | baseline 560, top tick 273.846; 12 heights checked against CSV class means; D10 YOLO11n corrected by 0.192 px, plot marker/payload aligned to visible 60 tick. No numeric source text changed.

The log figure is an image asset redrawn directly from all 150 archived epochs without smoothing; maxima are validated as 110, 92, 111. Tables do not create value-driven geometry and are excluded from the chart receipt.
