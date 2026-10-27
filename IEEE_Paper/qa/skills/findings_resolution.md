# Triage kết quả skill

## Công cụ thực sự được sử dụng

- `latex-paper-en`: compile runner (no shell escape), offline bibliography verification, figures, tables, five-element abstract, claim-forward, cross-section logic và experiment-writeup checks.
- `academic-paper-review`: deep reading, claim/evidence map, strengths/weaknesses và methodology review trong `qa/academic_review.md`.
- `nature-figure`: Python backend có sẵn, figure contracts/data mapping, render-time alignment, source preflight, PDF glyph và collision audits, final-size visual inspection.

## Các lỗi thực và kết quả sửa

- `audit_figure_collisions.py figures/paired_gaps_comparison.pdf …`, exit **1**: các hatch paths và một số grid lines đi qua vùng text trong PDF. Loại hatch, bỏ grid chỉ ở các panel có numeric annotations, rồi re-export. Không đổi dữ liệu, error bars hoặc giảm tolerance. Final collision audits: bốn hình đều PASS, không FAIL/WARN.
- `latex_compile.py main.tex --compiler xelatex --outdir build`, exit **12** ở lượt sớm: hai figure chưa sinh do figure QA dừng pipeline. Hoàn tất figure QA rồi chạy lại cùng compile runner. Final compile exit **0**.
- `validate_figure.py scripts/make_figures.py`, exit **1** ở lượt đầu: static regex không nhận DejaVu Sans dưới key tổng quát và không theo dõi được vòng lặp export extensions. Dùng cấu hình sans-serif rõ ràng với cùng DejaVu Sans và các export calls tường minh; xuất cả PNG/TIFF600dpi. Final source preflight: **21 PASS, 0 WARN, 0 FAIL**. Rendered QA được chạy lại sau thay đổi cấu hình.

## Wording/coherence diagnostics

Lượt đầu abstract analyzer không nhận hai câu background/objective vì dựa vào từ khoá. Dùng một chỉnh câu nhỏ về contrast/objective và nêu contribution ở cả Abstract/Conclusion, giữ nguyên facts. Bản cuối: background/objective/methods/results/conclusion đều PRESENT; script đếm206 words trong dải150–250. Claim-forward không phát hiện pattern; logic checker không còn rule-based coherence issue. Đây là các heuristic checks, không phải chứng nhận correctness.

## Cảnh báo được đánh giá theo phạm vi khoa học

- **Ablation/component evidence:** chưa có thí nghiệm tách component; bài không đề xuất component mới và không quy lợi ích riêng cho một thành phần kiến trúc. Giữ limitation, không tạo ablation giả.
- **“Promotional wording” ở RQ3:** đoạn đó là sparse-D40 support và việc không sửa label/split để tăng AP; đọc theo ngữ cảnh không phải marketing claim.
- **“Missing comparator” ở RQ4:** đoạn Results nêu rõ YOLOv8n và chênh lệch3,08/3,50pp; giữ comparator này và kiểm lại bảng.
- **“Missing variance” ở section heading:** bảng và text có sample SD qua ba seed; không thêm CI/p-value chỉ để đổi trạng thái detector.
- **Efficiency:** chưa đo, không kết luận và không thêm số đo. Không có detector-method claim yêu cầu efficiency comparison mới.
- **“Add causal analysis” ở Discussion:** giữ ba hướng giải thích của tác giả dưới dạng hypotheses và các control đề nghị. Không nâng correlation thành causal proof để đáp ứng từ khoá.
- **“Conclusion missing findings/implications”:** có numbered key quantitative findings và practical implications/future work trong hai đoạn; được đọc theo nội dung, không chỉ header.

## Bibliography

Offline check: 10 entries hợp lệ, 0 citation thiếu key. Có một entry gốc chưa dùng (`ultralyticsmetrics`) và khuyến nghị về DOI/truncation danh sách authors. Entry chưa dùng được giữ nguyên để không xoá source gốc không cần thiết. Không bịa DOI, không gọi offline syntax check là full-text/reference verification. PDF có chín references được trích dẫn, gồm tám key gốc và YOLO26.

Một số cảnh báo font khi IEEEtran khởi tạo XeLaTeX xuất hiện trước khi fontspec chọn font tài liệu. Kiểm PDF không thấy thiếu glyph, tên tác giả tiếng Việt hiển thị, và log cuối không có undefined citation/reference. Overfull vbox dưới2pt được kiểm bằng render; không có word box ra ngoài trang hoặc material horizontal clipping.
