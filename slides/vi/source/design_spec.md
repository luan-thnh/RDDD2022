<!-- ppt-master-schema: design-spec/v1 -->
# RDD2022 Research Editorial - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | RDD2022 Research Editorial |
| Canvas Format | PPT 16:9, 1280×720 |
| Page Count | 20 |
| Primary Language | vi-VN |
| Target Audience | Giảng viên, người phản biện, người nghe AI/thị giác máy tính |
| Communication Intent | Trình bày câu hỏi, giao thức, kết quả và giới hạn đã kiểm chứng |
| Desired Audience Outcome | Hiểu gap cùng tập đích và so sánh ba model, ba seed, từng lớp |
| Core Message / Ask / Action | YOLO26n tăng điểm tuyệt đối; gap xuyên miền vẫn lớn |
| Delivery Context | Có người thuyết trình bằng tiếng Việt; 20 slide / 8 phần |
| Artifact Afterlife | PPTX chỉnh sửa, PDF đọc trước và lưu trong RDDD2022 |
| Reading Mode | balanced |
| Content Strategy | Beautify 1:1: giữ mọi chữ, số, trang, thứ tự và notes nguồn |
| Design Style | research-editorial, free_design |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled — người dùng giao quyền tự quyết |
| Speaker Notes | enabled — giữ nguyên notes nguồn theo yêu cầu trước |
| Custom Animations | disabled — không được yêu cầu |
| Narration Audio | disabled — không được yêu cầu |
| Created Date | 2026-10-27 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280×720 |
| viewBox | `0 0 1280 720` |
| Margins | 56 px trái/phải, 28 px trên/dưới |
| Content Area | 56, 56 đến 1224, 684 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: briefing
- **Mode Behavior**: Nội dung nguyên văn và thứ tự của nguồn là thẩm quyền; đủ dữ liệu, chú thích và giới hạn ở đúng trang, không tái cấu trúc lập luận.
- **Visual style**: custom
- **Visual Style References**: editorial, swiss-minimal
- **Visual Style Behavior**: Tiêu đề serif có cấp bậc kiểu tạp chí, body và số liệu sans; đường kẻ và vùng trống tổ chức trang; căn lưới chính xác cho so sánh. Các ảnh chứng cứ và chart giữ vai trò chính, nền trắng với vùng phụ nhạt.
- **Theme**: Đường trao đổi hai miền tạo nhịp bìa/phương pháp, thay đổi theo trang; không lặp hộp kết luận dày.
- **Tone**: Khoa học, sáng, rõ ràng.

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFFFF | Nền chính |
| Secondary background | #F2F7F7 | Vùng phụ nhẹ |
| Primary | #173348 | Tiêu đề |
| Accent | #127B80 | Điểm nhấn và cùng miền |
| Secondary accent | #D89335 | YOLO26n |
| Body text | #173348 | Nội dung |
| Secondary text | #536778 | Chú thích |
| Divider | #DCE6EC | Kẻ và lưới |
| Comparison | #AABCC8 | Miền còn lại |
| Model second | #61899C | YOLOv8n |
| Model first | #176B87 | YOLO11n |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | Serif biên tập, rõ nét | Georgia | Georgia | Liberation Serif, serif |
| Body | Sans dễ đọc | Arial | Arial | Liberation Sans, sans-serif |

- **Title stack**: Georgia, Liberation Serif, serif
- **Body stack**: Arial, Liberation Sans, sans-serif

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 26.67 |
| Title | 40 |
| Subtitle | 28 |
| Annotation | 18 |
| Footer | 12 |
| Data | 22 |
| Kicker | 14 |
| Hero | 68 |
| Index | 36 |
| Domain label | 48 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: tiêu đề → chứng cứ → diễn giải → nguồn
- **Composition tendency**: phân chia bất đối xứng ở bìa/kết luận, so sánh đồng mức ở chart/ảnh
- **Cross-page continuity**: dòng section, nguồn và nhịp hình học ổn định; trọng lượng thay đổi theo công việc trang
- **Spacing posture**: mở ở bìa/kết luận, vừa ở bảng/chart, không làm loãng dữ liệu
- **Spacing anchors**: page margin 56; block gap 24; column gutter 40; corner radius 0; body leading 1.3

## VI. Icon Usage Specification

- **Primary bundled library**: none

| Icon Path | Suitable Scenarios |
| --- | --- |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| image1.png | 480×480 | 1.00 | Ví dụ Drone | Evidence | Toàn ảnh trên baseline chung, nhãn native bên ngoài | no-crop | user | Existing | Slide 3; ảnh validation gốc hoặc log vẽ lại từ CSV nguồn, không thêm chứng cứ |
| image2.png | 480×480 | 1.00 | Ví dụ MotorBike | Evidence | Toàn ảnh trên baseline chung, nhãn native bên ngoài | no-crop | user | Existing | Slide 3; ảnh validation gốc hoặc log vẽ lại từ CSV nguồn, không thêm chứng cứ |
| image3.png | 480×450 | 1.067 | Lớp D00 | Evidence | Toàn ảnh trên baseline chung, nhãn native bên ngoài | no-crop | user | Existing | Slide 7; ảnh validation gốc hoặc log vẽ lại từ CSV nguồn, không thêm chứng cứ |
| image4.png | 480×480 | 1.00 | Lớp D10 | Evidence | Toàn ảnh trên baseline chung, nhãn native bên ngoài | no-crop | user | Existing | Slide 7; ảnh validation gốc hoặc log vẽ lại từ CSV nguồn, không thêm chứng cứ |
| image5.png | 480×480 | 1.00 | Lớp D20 | Evidence | Toàn ảnh trên baseline chung, nhãn native bên ngoài | no-crop | user | Existing | Slide 7; ảnh validation gốc hoặc log vẽ lại từ CSV nguồn, không thêm chứng cứ |
| image6.png | 280×280 | 1.00 | Lớp D40 | Evidence | Toàn ảnh trên baseline chung, nhãn native bên ngoài | no-crop | user | Existing | Slide 7; ảnh validation gốc hoặc log vẽ lại từ CSV nguồn, không thêm chứng cứ |
| training_redrawn.png | 3200×1000 | 3.20 | Ba log huấn luyện vẽ lại từ CSV | Evidence | Toàn ảnh trên baseline chung, nhãn native bên ngoài | no-crop | user | Existing | Slide 12; ảnh validation gốc hoặc log vẽ lại từ CSV nguồn, không thêm chứng cứ |
| image8.png | 480×460 | 1.043 | Nhãn thật validation | Evidence | Toàn ảnh trên baseline chung, nhãn native bên ngoài | no-crop | user | Existing | Slide 17; ảnh validation gốc hoặc log vẽ lại từ CSV nguồn, không thêm chứng cứ |
| image9.png | 480×460 | 1.043 | Dự đoán validation | Evidence | Toàn ảnh trên baseline chung, nhãn native bên ngoài | no-crop | user | Existing | Slide 17; ảnh validation gốc hoặc log vẽ lại từ CSV nguồn, không thêm chứng cứ |

## IX. Content Outline

### Slide 01 - Phát hiện hư hỏng mặt đường
suy giảm bao nhiêu khi đổi miền thu nhận?

- **Audience move**: từ câu hỏi của trang đến hiểu phát hiện hư hỏng mặt đường
suy giảm bao nhiêu khi đổi miền thu nhận?.
- **Relationships**: link: Drone và MotorBike liên hệ hai chiều; membership: hai miền thuộc phạm vi nghiên cứu.
- **Composition**: Bìa chữ lớn bất đối xứng với đường trao đổi hai miền.
- **Title**: Phát hiện hư hỏng mặt đường
suy giảm bao nhiêu khi đổi miền thu nhận?
- **Core message**: Phát hiện hư hỏng mặt đường
suy giảm bao nhiêu khi đổi miền thu nhận?
- **Content**:
  - BÁO CÁO NGHIÊN CỨU · RDD2022
  - Phát hiện hư hỏng mặt đường / suy giảm bao nhiêu khi đổi miền thu nhận?
  - Nguồn: bản thảo hiện tại, IEEE_Paper/main.pdf · RDDD2022, 2026
  - 01
  - Đánh giá hai chiều Drone–MotorBike / với YOLO11n, YOLOv8n và YOLO26n
  - Lê Thành Luân · Phạm Bá Anh Tuấn / Trường Đại học Bách khoa – Đại học Đà Nẵng
  - Chia tập theo cảnh · Ba seed · 18 lượt huấn luyện
  - HAI MIỀN THU NHẬN
  - Drone
  - ↕
  - MotorBike
  - Hai tập đích cố định

### Slide 02 - Từ vấn đề triển khai đến bằng chứng thực nghiệm

- **Audience move**: từ câu hỏi của trang đến hiểu từ vấn đề triển khai đến bằng chứng thực nghiệm.
- **Relationships**: order: tám phần theo thứ tự của bản gốc.
- **Composition**: Mục lục theo trục đứng, tám mục chia hai cột.
- **Title**: Từ vấn đề triển khai đến bằng chứng thực nghiệm
- **Core message**: Từ vấn đề triển khai đến bằng chứng thực nghiệm
- **Content**:
  - LỘ TRÌNH TRÌNH BÀY
  - Từ vấn đề triển khai đến bằng chứng thực nghiệm
  - RDD2022 · Đánh giá hai chiều trên cùng tập đích · Bản trình bày nghiên cứu, 2026
  - 02
  - 01
  - Đặt vấn đề
  - Slide 03–04
  - 02
  - Mục tiêu nghiên cứu
  - Slide 05
  - 03
  - Dữ liệu nghiên cứu
  - Slide 06–08
  - 04
  - Phương pháp nghiên cứu
  - Slide 09–10
  - 05
  - Mô hình và huấn luyện
  - Slide 11–12
  - 06
  - Kết quả thực nghiệm
  - Slide 13–17
  - 07
  - Hạn chế nghiên cứu
  - Slide 18
  - 08
  - Kết luận và hướng phát triển
  - Slide 19–20

### Slide 03 - Đổi nền tảng thu nhận làm thay đổi bối cảnh quan sát

- **Audience move**: từ câu hỏi của trang đến hiểu đổi nền tảng thu nhận làm thay đổi bối cảnh quan sát.
- **Relationships**: contrast: hai miền thu nhận, cùng bài toán.
- **Composition**: Ảnh đối chiếu lớn, nhãn cùng baseline, kết luận ở mép dưới.
- **Title**: Đổi nền tảng thu nhận làm thay đổi bối cảnh quan sát
- **Core message**: Đổi nền tảng thu nhận làm thay đổi bối cảnh quan sát
- **Content**:
  - 01 · ĐẶT VẤN ĐỀ
  - Đổi nền tảng thu nhận làm thay đổi bối cảnh quan sát
  - Nguồn ảnh: YOLO11n D13/M13, run/val_batch0_labels.jpg · Ví dụ validation có nhãn gốc
  - 03
  - Drone · góc nhìn từ trên
  - MotorBike · góc nhìn mặt đường
  - Cùng bài toán / Khác góc nhìn / Khác cảnh / Khác phân bố dữ liệu
  - Hiệu năng trên dữ liệu giống miền huấn luyện chưa đủ để bảo đảm khi triển khai sang miền khác.
- **Images**: image1.png, image2.png; giữ đầy đủ khung/nhãn.

### Slide 04 - Bốn câu hỏi cần trả lời bằng cùng một giao thức

- **Audience move**: từ câu hỏi của trang đến hiểu bốn câu hỏi cần trả lời bằng cùng một giao thức.
- **Relationships**: membership: RQ1–RQ4 thuộc cùng giao thức.
- **Composition**: Bốn câu hỏi là bốn đoạn độc lập có chỉ mục nổi bật.
- **Title**: Bốn câu hỏi cần trả lời bằng cùng một giao thức
- **Core message**: Bốn câu hỏi cần trả lời bằng cùng một giao thức
- **Content**:
  - 01 · ĐẶT VẤN ĐỀ
  - Bốn câu hỏi cần trả lời bằng cùng một giao thức
  - Nguồn: paper hiện tại, phần I · RQ1–RQ4
  - 04
  - RQ1
  - Gap lớn bao nhiêu và có bất đối xứng giữa hai tập đích?
  - RQ2
  - Chiều và độ lớn gap có ổn định qua seed và ba model?
  - RQ3
  - D00, D10, D20, D40 suy giảm khác nhau như thế nào?
  - RQ4
  - YOLO26n tăng độ chính xác tuyệt đối có làm giảm gap?
  - Giả thuyết kiểm tra: huấn luyện trên miền đích có lợi thế dương khi đánh giá trên cùng ảnh đích.

### Slide 05 - Định lượng khả năng chuyển miền, kiểm tra tính lặp lại

- **Audience move**: từ câu hỏi của trang đến hiểu định lượng khả năng chuyển miền, kiểm tra tính lặp lại.
- **Relationships**: membership: bốn mục tiêu thuộc phạm vi 18 lượt.
- **Composition**: Khối mục tiêu gọn và phạm vi nổi bật bên dưới.
- **Title**: Định lượng khả năng chuyển miền, kiểm tra tính lặp lại
- **Core message**: Định lượng khả năng chuyển miền, kiểm tra tính lặp lại
- **Content**:
  - 02 · MỤC TIÊU NGHIÊN CỨU
  - Định lượng khả năng chuyển miền, kiểm tra tính lặp lại
  - Nguồn: paper hiện tại, mục tiêu và đóng góp; thiết kế 18 lượt huấn luyện
  - 05
  - Đo hai chiều
  - Giữ cố định từng tập đích khi so sánh.
  - Kiểm tra độ ổn định
  - Ghép cặp seed 13, 37, 71 trên ba model.
  - Phân tích theo lớp
  - Giữ đủ bốn lớp, kể cả kết quả bất lợi.
  - Mở rộng bằng YOLO26n
  - So sánh độ chính xác và gap với hai model trước.
  - Phạm vi: 2 miền × 3 model × 3 seed = 18 lượt huấn luyện; mỗi lượt được đánh giá trên cả hai tập đích.

### Slide 06 - Tập con khóa v4.1 gồm 4.378 ảnh và 658 ảnh test

- **Audience move**: từ câu hỏi của trang đến hiểu tập con khóa v4.1 gồm 4.378 ảnh và 658 ảnh test.
- **Relationships**: contrast: số ảnh từng phân vùng ở hai miền.
- **Composition**: Bảng số liệu lớn, summary hàng cuối có nhấn.
- **Title**: Tập con khóa v4.1 gồm 4.378 ảnh và 658 ảnh test
- **Core message**: Tập con khóa v4.1 gồm 4.378 ảnh và 658 ảnh test
- **Content**:
  - 03 · DỮ LIỆU NGHIÊN CỨU
  - Tập con khóa v4.1 gồm 4.378 ảnh và 658 ảnh test
  - Nguồn: paper, Bảng I và phần II · Số ảnh của tập con khóa, không phải toàn bộ RDD2022
  - 06
  - Chia tập theo nhóm cảnh; cùng manifest khóa cho ba model và ba seed.
  - Test được giữ cố định theo từng miền để so sánh hai nguồn huấn luyện trên cùng quần thể ảnh.
  - Miền | Train | Validation | Test | Tổng
  - Drone | 1.680 | 360 | 361 | 2.401
  - MotorBike | 1.383 | 297 | 297 | 1.977
  - Tổng | 3.063 | 657 | 658 | 4.378
- **Visualization**: data-table: bảng nguyên văn nguồn trang 6.
- **Native-ready**: data-table=yes

### Slide 07 - Bốn loại hư hỏng được giữ thống nhất trong đánh giá

- **Audience move**: từ câu hỏi của trang đến hiểu bốn loại hư hỏng được giữ thống nhất trong đánh giá.
- **Relationships**: membership: D00, D10, D20, D40 thuộc bốn lớp đích.
- **Composition**: Bốn ví dụ chứng cứ theo dải ảnh trên một baseline.
- **Title**: Bốn loại hư hỏng được giữ thống nhất trong đánh giá
- **Core message**: Bốn loại hư hỏng được giữ thống nhất trong đánh giá
- **Content**:
  - 03 · DỮ LIỆU NGHIÊN CỨU
  - Bốn loại hư hỏng được giữ thống nhất trong đánh giá
  - Nguồn: ảnh nhãn validation YOLO11n D13/M13 · Crop giữ nhãn gốc; D40 được phóng vùng có nhãn
  - 07
  - D00
  - Nứt dọc
  - D10
  - Nứt ngang
  - D20
  - Nứt da cá sấu
  - D40
  - Ổ gà
- **Images**: image3.png, image4.png, image5.png, image6.png; giữ đầy đủ khung/nhãn.

### Slide 08 - Số hộp nhãn và mức hỗ trợ lớp khác nhau giữa hai miền

- **Audience move**: từ câu hỏi của trang đến hiểu số hộp nhãn và mức hỗ trợ lớp khác nhau giữa hai miền.
- **Relationships**: contrast: số hộp nhãn giữa hai tập đích; link: hỗ trợ thưa với bất định D40.
- **Composition**: Bảng mở và điểm hỗ trợ D40 ở vùng riêng.
- **Title**: Số hộp nhãn và mức hỗ trợ lớp khác nhau giữa hai miền
- **Core message**: Số hộp nhãn và mức hỗ trợ lớp khác nhau giữa hai miền
- **Content**:
  - 03 · DỮ LIỆU NGHIÊN CỨU
  - Số hộp nhãn và mức hỗ trợ lớp khác nhau giữa hai miền
  - Nguồn: paper, Bảng II · Số bounding box của bốn lớp trên tập test khóa
  - 08
  - D40 trên Drone
  - 17 hộp / 9 ảnh
  - Phân bố lớp không cân bằng; AP của lớp hiếm có thể nhạy với một số ít phát hiện.
  - Không quy toàn bộ khác biệt hiệu năng cho góc nhìn: dữ liệu và thành phần cảnh cùng thay đổi.
  - Tập đích | D00 | D10 | D20 | D40
  - Drone Test | 214 | 189 | 44 | 17
  - MotorBike Test | 403 | 165 | 96 | 35
- **Visualization**: data-table: bảng nguyên văn nguồn trang 8.
- **Native-ready**: data-table=yes

### Slide 09 - Giao thức hai chiều so sánh trên cùng tập đích

- **Audience move**: từ câu hỏi của trang đến hiểu giao thức hai chiều so sánh trên cùng tập đích.
- **Relationships**: order: rà soát cảnh → khóa phân vùng → fine-tune; contrast: hai nguồn huấn luyện trên cùng tập đích.
- **Composition**: Ba bước trên một trục, ma trận đích dưới trục.
- **Title**: Giao thức hai chiều so sánh trên cùng tập đích
- **Core message**: Giao thức hai chiều so sánh trên cùng tập đích
- **Content**:
  - 04 · PHƯƠNG PHÁP NGHIÊN CỨU
  - Giao thức hai chiều so sánh trên cùng tập đích
  - Nguồn: paper, phần II · Chia tập theo cảnh; checkpoint chọn bằng validation miền nguồn
  - 09
  - Rà soát cảnh
  - Giữ nhóm cảnh / trong một phân vùng
  - →
  - Khóa phân vùng
  - Train / validation / test / cho từng miền
  - →
  - Fine-tune độc lập
  - 3 model × 2 miền / × 3 seed
  - Trong mỗi cột test, hai mô hình được chấm trên cùng ảnh; ghép cặp theo seed khi tính gap.
  - Nguồn huấn luyện | Drone Test · 361 ảnh | MotorBike Test · 297 ảnh
  - Drone | Cùng miền: D → D | Xuyên miền: D → M
  - MotorBike | Xuyên miền: M → D | Cùng miền: M → M
- **Visualization**: data-table: bảng nguyên văn nguồn trang 9.
- **Native-ready**: data-table=yes

### Slide 10 - Gap được tính bằng chênh lệch trên cùng ảnh đích

- **Audience move**: từ câu hỏi của trang đến hiểu gap được tính bằng chênh lệch trên cùng ảnh đích.
- **Relationships**: link: hai mAP trên cùng tập đích tạo gap ghép cặp.
- **Composition**: Công thức là điểm nhìn trung tâm, hai vùng diễn giải.
- **Title**: Gap được tính bằng chênh lệch trên cùng ảnh đích
- **Core message**: Gap được tính bằng chênh lệch trên cùng ảnh đích
- **Content**:
  - 04 · PHƯƠNG PHÁP NGHIÊN CỨU
  - Gap được tính bằng chênh lệch trên cùng ảnh đích
  - Nguồn: paper, định nghĩa fixed-target gap và Bảng V · Đơn vị gap: điểm phần trăm (pp)
  - 10
  - G(Y) = mAP(Y → Y) − mAP(X → Y)
  - Chỉ số chính
  - mAP@50:95 (%) / Trung bình AP của 4 lớp / trên các ngưỡng IoU 0,50–0,95
  - Cách tổng hợp
  - Gap cho từng seed ghép cặp / Báo cáo trung bình ± SD / SD qua 3 seed, không phải CI
  - G(Y) > 0: huấn luyện trên miền đích có lợi thế; giảm tương đối (%) = 100 × G(Y) / mAP(Y → Y).

### Slide 11 - Ba biến thể nano dùng chung cấu hình fine-tune tường minh

- **Audience move**: từ câu hỏi của trang đến hiểu ba biến thể nano dùng chung cấu hình fine-tune tường minh.
- **Relationships**: membership: ba model dùng cùng cấu hình tường minh.
- **Composition**: Tên ba model dạng masthead, bảng cấu hình thoáng.
- **Title**: Ba biến thể nano dùng chung cấu hình fine-tune tường minh
- **Core message**: Ba biến thể nano dùng chung cấu hình fine-tune tường minh
- **Content**:
  - 05 · MÔ HÌNH VÀ HUẤN LUYỆN
  - Ba biến thể nano dùng chung cấu hình fine-tune tường minh
  - Nguồn: paper, thiết lập thực nghiệm; data/training_audit.csv · 18/18 log đủ 150 epoch
  - 11
  - YOLO11n
  - YOLOv8n
  - YOLO26n
  - Seed dùng lại: 13, 37, 71; mỗi model có 2 miền huấn luyện × 3 seed = 6 lượt.
  - Thành phần | Cấu hình
  - Khởi tạo / thư viện | COCO-pretrained · Ultralytics 8.4.190
  - Ngân sách | 150 epoch · batch 8 · ảnh 640 · patience = 0
  - Tối ưu | SGD · lr 0,01 · momentum 0,937 · weight decay 0,0005
  - Biến đổi ảnh | Tắt mosaic, mixup, HSV · translate 0,05 · scale 0,15 · fliplr 0,5
- **Visualization**: data-table: bảng nguyên văn nguồn trang 11.
- **Native-ready**: data-table=yes

### Slide 12 - Log đủ 150 epoch; đỉnh validation xuất hiện trước khi kết thúc

- **Audience move**: từ câu hỏi của trang đến hiểu log đủ 150 epoch; đỉnh validation xuất hiện trước khi kết thúc.
- **Relationships**: order: log theo epoch; contrast: ba seed.
- **Composition**: Ba biểu đồ log vẽ lại cùng chiều cao và trục epoch.
- **Title**: Log đủ 150 epoch; đỉnh validation xuất hiện trước khi kết thúc
- **Core message**: Log đủ 150 epoch; đỉnh validation xuất hiện trước khi kết thúc
- **Content**:
  - 05 · MÔ HÌNH VÀ HUẤN LUYỆN
  - Log đủ 150 epoch; đỉnh validation xuất hiện trước khi kết thúc
  - Vẽ lại từ log YOLO11n–Drone, seed 13/37/71 · Tương ứng paper, Hình 1; đường không làm mượt
  - 12
  - YOLO11n–Drone: đỉnh mAP validation ở epoch 110 / 92 / 111.
  - Các điểm tròn là cực đại mAP validation được ghi trong log; chưa chứng minh hội tụ tối ưu toàn cục.
- **Images**: training_redrawn.png; giữ đầy đủ khung/nhãn.

### Slide 13 - Huấn luyện đúng miền đích có lợi thế ở cả ba model

- **Audience move**: từ câu hỏi của trang đến hiểu huấn luyện đúng miền đích có lợi thế ở cả ba model.
- **Relationships**: contrast: cùng miền và miền còn lại trên từng tập đích.
- **Composition**: Hai tập đích cạnh nhau, scale bằng nhau, vạch SD được giữ.
- **Title**: Huấn luyện đúng miền đích có lợi thế ở cả ba model
- **Core message**: Huấn luyện đúng miền đích có lợi thế ở cả ba model
- **Content**:
  - 06 · KẾT QUẢ THỰC NGHIỆM
  - Huấn luyện đúng miền đích có lợi thế ở cả ba model
  - Nguồn: paper, Bảng III / Hình 4; data/all_metrics.csv · mAP@50:95 (%), trung bình ± SD, n = 3
  - 13
  - Drone Test
  - YOLO11n
  - 22.39 ± 1.82
  - 7.25 ± 3.64
  - YOLOv8n
  - 21.41 ± 1.71
  - 6.55 ± 2.59
  - YOLO26n
  - 24.49 ± 0.74
  - 7.58 ± 0.15
  - 0
  - 20
  - 40
  - 60
  - MotorBike Test
  - YOLO11n
  - 53.08 ± 0.44
  - 10.15 ± 0.43
  - YOLOv8n
  - 51.25 ± 0.31
  - 10.01 ± 1.21
  - YOLO26n
  - 54.75 ± 1.24
  - 12.48 ± 0.13
  - 0
  - 20
  - 40
  - 60
  - Huấn luyện trên miền đích
  - Huấn luyện trên miền còn lại
  - YOLO26n tăng mean cùng miền so với YOLOv8n: +3,08 pp trên Drone và +3,50 pp trên MotorBike.
- **Visualization**: drone-performance: cột và SD cùng scale; motorbike-performance: cột và SD cùng scale.
- **Native-ready**: drone-performance=no; motorbike-performance=no

### Slide 14 - Cả 18 gap theo seed đều dương; MotorBike có gap lớn hơn

- **Audience move**: từ câu hỏi của trang đến hiểu cả 18 gap theo seed đều dương; motorbike có gap lớn hơn.
- **Relationships**: contrast: gap theo model và tập đích; membership: ba seed trong mỗi phép so sánh.
- **Composition**: Một plot đủ 18 điểm, vùng hai target phân biệt bằng khoảng trống.
- **Title**: Cả 18 gap theo seed đều dương; MotorBike có gap lớn hơn
- **Core message**: Cả 18 gap theo seed đều dương; MotorBike có gap lớn hơn
- **Content**:
  - 06 · KẾT QUẢ THỰC NGHIỆM
  - Cả 18 gap theo seed đều dương; MotorBike có gap lớn hơn
  - Nguồn: paper, Bảng V–VI; data/fixed_target_gaps_by_seed.csv · Mỗi điểm là một seed; đơn vị pp
  - 14
  - 0
  - 10
  - 20
  - 30
  - 40
  - 50
  - Drone · YOLO11n
  - 15.13
  - Drone · YOLOv8n
  - 14.86
  - Drone · YOLO26n
  - 16.91
  - MotorBike · YOLO11n
  - 42.94
  - MotorBike · YOLOv8n
  - 41.24
  - MotorBike · YOLO26n
  - 42.27
  - Gap TB
  - Mean gap: Drone 14,86–16,91 pp; MotorBike 41,24–42,94 pp. Mỗi phép so sánh giữ cùng tập đích.
- **Visualization**: seed-gap: 18 điểm và khoảng min–max từ seed.
- **Native-ready**: seed-gap=no

### Slide 15 - D20 trên MotorBike mất nhiều AP; D40 trên Drone đảo chiều

- **Audience move**: từ câu hỏi của trang đến hiểu d20 trên motorbike mất nhiều ap; d40 trên drone đảo chiều.
- **Relationships**: contrast: gap theo lớp trên MotorBike; ngoại lệ D40 trên Drone.
- **Composition**: Biểu đồ lớp chiếm phần lớn trang, ngoại lệ D40 có vùng riêng.
- **Title**: D20 trên MotorBike mất nhiều AP; D40 trên Drone đảo chiều
- **Core message**: D20 trên MotorBike mất nhiều AP; D40 trên Drone đảo chiều
- **Content**:
  - 06 · KẾT QUẢ THỰC NGHIỆM
  - D20 trên MotorBike mất nhiều AP; D40 trên Drone đảo chiều
  - Nguồn: paper, Bảng VII / Hình 3; AP@50:95 mean qua 3 seed · Gap tính trên cùng tập đích
  - 15
  - Gap theo lớp trên MotorBike Test (pp)
  - 0
  - 20
  - 40
  - 60
  - D00
  - D10
  - 57.7
  - 53.2
  - 56.4
  - D20
  - D40
  - YOLO11n
  - YOLOv8n
  - YOLO26n
  - Ngoại lệ D40 · Drone
  - YOLO11n   −6,61 pp / YOLOv8n   −9,74 pp / YOLO26n   −1,95 pp
  - Hỗ trợ thưa: 17 hộp / 9 ảnh. / Giữ nguyên kết quả này.
  - D20 trên MotorBike: giảm AP tương đối 96,14–98,30% so với baseline huấn luyện trên MotorBike.
- **Visualization**: class-gap: 4 lớp × 3 model, mean gap MotorBike.
- **Native-ready**: class-gap=yes

### Slide 16 - Lọc ảnh có nhãn ngoài phạm vi vẫn giữ chiều gap

- **Audience move**: từ câu hỏi của trang đến hiểu lọc ảnh có nhãn ngoài phạm vi vẫn giữ chiều gap.
- **Relationships**: contrast: gap full và clean-only theo hai tập đích.
- **Composition**: Bảng kiểm tra độ nhạy có hàng YOLO26n nổi bật.
- **Title**: Lọc ảnh có nhãn ngoài phạm vi vẫn giữ chiều gap
- **Core message**: Lọc ảnh có nhãn ngoài phạm vi vẫn giữ chiều gap
- **Content**:
  - 06 · KẾT QUẢ THỰC NGHIỆM
  - Lọc ảnh có nhãn ngoài phạm vi vẫn giữ chiều gap
  - Nguồn: paper, phần IV; data/gap_summary.csv · Clean-only: Drone 273 ảnh, MotorBike 271 ảnh
  - 16
  - Cả 18 so sánh clean-only vẫn dương; bảng ghi mean gap (pp), n = 3.
  - Clean-only thay đổi thành phần ảnh test; chưa thể quy phần thay đổi metric chỉ cho tác động của nhãn bị lọc.
  - Model | Drone: full | Drone: clean | MotorBike: full | MotorBike: clean
  - YOLO11n | 15.13 | 14.93 | 42.94 | 43.86
  - YOLOv8n | 14.86 | 15.25 | 41.24 | 41.87
  - YOLO26n | 16.91 | 16.59 | 42.27 | 42.60
- **Visualization**: data-table: bảng nguyên văn nguồn trang 16.
- **Native-ready**: data-table=yes

### Slide 17 - Ảnh lưu trữ minh họa nhãn thật và dự đoán validation

- **Audience move**: từ câu hỏi của trang đến hiểu ảnh lưu trữ minh họa nhãn thật và dự đoán validation.
- **Relationships**: contrast: GT và dự đoán trên cùng ảnh validation.
- **Composition**: Cặp GT/pred lớn cân bằng, chú giải cùng ảnh ở mép phải.
- **Title**: Ảnh lưu trữ minh họa nhãn thật và dự đoán validation
- **Core message**: Ảnh lưu trữ minh họa nhãn thật và dự đoán validation
- **Content**:
  - 06 · KẾT QUẢ THỰC NGHIỆM
  - Ảnh lưu trữ minh họa nhãn thật và dự đoán validation
  - Nguồn: YOLO11n MotorBike seed 13 · run/val_batch0_{labels,pred}.jpg · China_MotorBike_001773.jpg
  - 17
  - Nhãn thật (GT)
  - Dự đoán được lưu
  - Cùng một ảnh / Cùng miền nguồn / Khung và điểm / giữ như bản lưu
  - Ví dụ minh họa validation; chưa thay thế kiểm tra FP/FN độc lập trên ảnh test xuyên miền.
- **Images**: image8.png, image9.png; giữ đầy đủ khung/nhãn.

### Slide 18 - Bằng chứng còn bị giới hạn bởi cảnh, nguồn và cách kiểm chứng

- **Audience move**: từ câu hỏi của trang đến hiểu bằng chứng còn bị giới hạn bởi cảnh, nguồn và cách kiểm chứng.
- **Relationships**: membership: bốn giới hạn của bằng chứng.
- **Composition**: Hai cột giới hạn với nhịp và phân cấp rõ.
- **Title**: Bằng chứng còn bị giới hạn bởi cảnh, nguồn và cách kiểm chứng
- **Core message**: Bằng chứng còn bị giới hạn bởi cảnh, nguồn và cách kiểm chứng
- **Content**:
  - 07 · HẠN CHẾ CỦA NGHIÊN CỨU
  - Bằng chứng còn bị giới hạn bởi cảnh, nguồn và cách kiểm chứng
  - Nguồn: paper, phần V · Giới hạn được giữ cùng các kết quả thuận và bất lợi
  - 18
  - Yếu tố cùng thay đổi
  - Góc nhìn, cỡ tập train, cảnh và phân bố lớp chưa được tách riêng.
  - Phạm vi lặp lại hẹp
  - Ba seed và ba biến thể cùng họ; SD chưa phản ánh bất định theo cảnh.
  - Kiểm soát cảnh chưa tuyệt đối
  - Bảo vệ liên kết đã nhận diện; từng xem một số ảnh MotorBike trước khi khóa split.
  - Chưa replay độc lập
  - Chưa chạy lại inference/test hoặc audit ảnh–XML; D40 trên Drone có hỗ trợ thưa.

### Slide 19 - YOLO26n tăng điểm tuyệt đối, gap xuyên miền vẫn lớn

- **Audience move**: từ câu hỏi của trang đến hiểu yolo26n tăng điểm tuyệt đối, gap xuyên miền vẫn lớn.
- **Relationships**: link: độ chính xác tuyệt đối tăng cùng với gap còn lớn; contrast: gap hai tập đích.
- **Composition**: Hai khoảng gap cỡ lớn bên trái, kiểm tra lặp lại bên phải.
- **Title**: YOLO26n tăng điểm tuyệt đối, gap xuyên miền vẫn lớn
- **Core message**: YOLO26n tăng điểm tuyệt đối, gap xuyên miền vẫn lớn
- **Content**:
  - 08 · KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN
  - YOLO26n tăng điểm tuyệt đối, gap xuyên miền vẫn lớn
  - Nguồn: paper, Kết luận; Bảng III, V, VI, VII · Các kết luận mang tính mô tả trên split khóa
  - 19
  - 14,86–16,91 pp
  - Mean gap trên Drone Test
  - 41,24–42,94 pp
  - Mean gap trên MotorBike Test
  - 18/18 so sánh dương
  - Lặp lại ở ba model. / D20 dễ tổn thương trên MotorBike. / D40 hiếm trên Drone có đảo chiều.
  - Đóng góp: giao thức hai chiều trên cùng tập đích, minh bạch theo seed và kiểm tra lặp lại với YOLO26n.

### Slide 20 - Bước tiếp theo: kiểm chứng độc lập và tách yếu tố gây nhiễu

- **Audience move**: từ câu hỏi của trang đến hiểu bước tiếp theo: kiểm chứng độc lập và tách yếu tố gây nhiễu.
- **Relationships**: order: bốn công việc tương lai theo ưu tiên.
- **Composition**: Bốn ưu tiên theo trục đọc, câu trao đổi đóng trang.
- **Title**: Bước tiếp theo: kiểm chứng độc lập và tách yếu tố gây nhiễu
- **Core message**: Bước tiếp theo: kiểm chứng độc lập và tách yếu tố gây nhiễu
- **Content**:
  - 08 · KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN
  - Bước tiếp theo: kiểm chứng độc lập và tách yếu tố gây nhiễu
  - Nguồn: paper, Thảo luận và hướng phát triển · Các mục dưới đây là công việc đề xuất
  - 20
  - 01
  - Kiểm chứng dự đoán
  - Replay checkpoint; lưu dự đoán từng ảnh; audit FP/FN và bootstrap theo cảnh.
  - 02
  - Bổ sung đối chứng
  - Cân bằng cỡ tập nguồn; thu cùng đoạn đường với nhiều góc nhìn.
  - 03
  - Mở rộng có kiểm soát
  - Rà ontology nhãn trước khi đánh giá Czech, India hoặc bộ dữ liệu độc lập.
  - 04
  - Thử biện pháp cải thiện
  - Huấn luyện đa miền hoặc thích nghi miền; chấm lại bằng giao thức cố định.
  - Trao đổi: đối chứng nào cần được ưu tiên trước khi khẳng định khả năng triển khai?

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: mỗi SVG và notes cùng stem
- **Content**: giữ nguyên notes từng trang từ sources/RDD2022_Bao_cao_Tieng_Viet.pptx; preserve verbatim
- **Total duration**: khoảng 12–15 phút, người trình bày điều chỉnh
- **Notes style**: tiếng Việt, khoa học và tự nhiên
- **Presentation purpose**: giải thích giao thức, kết quả và giới hạn thực nghiệm
