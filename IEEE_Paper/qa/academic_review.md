# Tự phản biện bản tích hợp theo bộ skill paper

Đây là review hỗ trợ chỉnh sửa, không phải phản biện độc lập của hội nghị và không dự đoán khả năng được nhận.

## Metadata và phạm vi

- Empirical descriptive evaluation về road-damage detection trên RDD2022.
- Định dạng IEEE conference A4; chưa biết hội nghị hoặc giới hạn trang cụ thể.
- Đọc source trước YOLO26, flow chỉnh sửa trong hồ sơ hội thoại và bản tích hợp; đối chiếu kết quả 18 run đã lưu.
- Câu hỏi: hoàn thiện bản đang viết dở bằng chứng YOLO26, bảo toàn mạch khoa học của bản nền.

## Claims và mức bằng chứng

1. **Cùng target, target-trained tốt hơn other-domain-trained ở mAP chung:** được hỗ trợ bởi cả 18 seed-specific gaps trên full test; clean-only giữ chiều. Đây là metric-level reanalysis trên tập cố định.
2. **Gap lớn hơn khi target là MotorBike:** được hỗ trợ trong ba biến thể; chênh lệch hai target-gap 25,36–27,80 pp. Không phải hiệu ứng nhân quả riêng của hướng camera.
3. **Class heterogeneity:** được hỗ trợ bởi bảng AP và per-seed differences; D20 MotorBike giảm mạnh, D40 Drone có mean gap âm và hỗ trợ lớp ít. Cơ chế fine texture/scale chưa được tách bằng thí nghiệm.
4. **YOLO26 tăng in-domain mean accuracy nhưng không xoá gap:** được hỗ trợ bởi cùng split và mean qua ba seed. Không phải kết luận kiến trúc mới luôn tốt hơn mọi lớp, không chứng minh SOTA hay ý nghĩa thống kê của chênh lệch nhỏ.

## Điểm mạnh

- **S1 — Estimand rõ:** Eq. (1) giữ nguyên target images trong mỗi phép so sánh, tránh lấy hai test population khác nhau làm một gap.
- **S2 — Evidence trong main:** bảy bảng giữ số liệu seed/class/complementary metric để người đọc kiểm chứng trực tiếp; YOLO26 được thêm vào cùng cấu trúc bảng.
- **S3 — Replication và kết quả bất lợi được giữ:** ba seed dùng lại cho ba biến thể; không giấu D40 gap âm hay trường hợp D20 của YOLO11 cao hơn YOLO26.
- **S4 — Nội dung và hình đồng bộ:** bốn hình có mục đích khác nhau; source data, SD definition, label/citation closure và rendered QA được giữ kèm.

## Hạn chế còn lại và cách xử lý phù hợp

- **W1 — Confounds nguồn:** size, scene/location, illumination và annotation có thể cùng thay đổi. Bản thảo giữ claims ở mức domain-associated, đề xuất size-matched control hoặc paired-view work; không giả định đã có ablation.
- **W2 — Đơn vị và độ bất định:** ba seed không phải các road-site độc lập. Bản thảo báo sample SD, không gọi đó là CI/p-value hoặc bỏ seed để có kết quả đẹp.
- **W3 — Sparse class/audit:** D40 Drone hỗ trợ ít; scene review có giới hạn và test exposure trước lock. Các điểm này được giữ trong RQ3 và Threats, không thay label/split.
- **W4 — Phạm vi tái lập:** CSV/JSON và training logs đã kiểm nhưng chưa independently replay inference từ checkpoint hoặc audit lại ảnh/XML. Data availability/Threats giữ đúng ranh giới.

## Methodology assessment

| Tiêu chí | Đánh giá theo bằng chứng hiện có |
|---|---|
| Soundness | Fixed-target definition và số bảng đã được kiểm độc lập với raw retained rows. |
| Novelty | Là descriptive extension/replication; chưa làm systematic novelty search và không dùng claim “chưa ai làm”. |
| Reproducibility | Tái tạo được bảng/hình/PDF từ CSV đã giao; chưa xác minh tái tạo toàn bộ data audit/training/inference. |
| Experimental design | Source comparison rõ; size/scene/platform confounds và chỉ một họ detector được ghi nhận. |
| Statistics | Mean/sample SD và seed pairing được tính đúng; formal population inference ngoài phạm vi. |
| Efficiency | Chưa đo latency/compute. Không thêm số Params/FLOPs hay efficiency claim chưa được đối chiếu theo cùng chuẩn. |

Không quy đổi bảng này thành điểm chất lượng hoặc xác suất acceptance: chưa có venue/rubric và chưa kiểm chứng toàn bộ raw pipeline.

## Literature positioning và source boundaries

Giữ các trích dẫn tác giả đã dùng, thêm đúng reference YOLO26; chuyển COCO về vai trò pretraining. Những câu không được literature coverage hỗ trợ được thu hẹp, không thay bằng tuyên bố “SOTA”. Tài liệu dự án/author summaries và model documentation có từ giai đoạn đối chiếu trước; chưa xác minh lại toàn văn mọi paper. Không gửi metadata citation tới third-party API trong lần này.

## Kết quả sửa

Bản tích hợp đáp ứng flow đã xác định: bốn RQ, YOLO evolution, ba-model Results/RQ4, Limitations/Threats; giữ khung Consensus/Trade-off/Gap/This paper, training, giải thích scale/context/class, prior-work comparison và các bảng trong main. Title, authors, equations, labels và cited keys gốc được kiểm bảo toàn bằng script. Các điều chỉnh numerical/claim level có trong diff và integration map.

Các việc tác giả cần chốt cho submission là venue/page limit, declarations và khả năng cung cấp raw split/audit/inference artifacts theo yêu cầu nơi nộp. Không thêm thí nghiệm giả hoặc mở rộng bài sang một nghiên cứu khác để thoả cảnh báo heuristic.
