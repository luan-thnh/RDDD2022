<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## communication
- primary_language: vi-VN
- audience: Giảng viên, người phản biện và người nghe nghiên cứu AI
- objective: Trình bày đủ giao thức, dữ liệu và giới hạn để người nghe hiểu gap cùng tập đích và so sánh ba model.
- core_message: YOLO26n tăng điểm tuyệt đối; gap xuyên miền vẫn lớn.
- consumption_mode: balanced

## mode
- mode: custom
- mode_references: briefing
- mode_behavior: Giữ mọi chữ và thứ tự 20 trang của nguồn; thông tin đủ và rõ, không tái cấu trúc.

## visual_style
- visual_style: custom
- visual_style_references: editorial, swiss-minimal
- visual_style_behavior: Tiêu đề serif kiểu tạp chí, body sans; vùng trắng và đường kẻ mảnh, căn lưới chính xác ở các so sánh; chart và ảnh là chứng cứ lớn.

## colors
- background: #FFFFFF
- secondary_bg: #F2F7F7
- primary: #173348
- accent: #127B80
- secondary_accent: #D89335
- body_text: #173348
- secondary_text: #536778
- divider: #DCE6EC
- comparison: #AABCC8
- model_first: #176B87
- model_second: #61899C

## typography
- font_family: Arial, Liberation Sans, sans-serif
- title_family: Georgia, Liberation Serif, serif
- body_family: Arial, Liberation Sans, sans-serif
- body: 26.67
- title: 40
- subtitle: 28
- annotation: 18
- footer: 12
- data: 22
- kicker: 14
- hero: 68
- index: 36
- domain_label: 48

## icons
- library: none
- inventory: none

## images
- image1: images/image1.png | source=user | crop=no-crop
- image2: images/image2.png | source=user | crop=no-crop
- image3: images/image3.png | source=user | crop=no-crop
- image4: images/image4.png | source=user | crop=no-crop
- image5: images/image5.png | source=user | crop=no-crop
- image6: images/image6.png | source=user | crop=no-crop
- image7: images/training_redrawn.png | source=user | crop=no-crop
- image8: images/image8.png | source=user | crop=no-crop
- image9: images/image9.png | source=user | crop=no-crop

## page_rhythm
- P01: anchor
- P02: anchor
- P03: dense
- P04: dense
- P05: dense
- P06: dense
- P07: dense
- P08: dense
- P09: dense
- P10: dense
- P11: dense
- P12: dense
- P13: dense
- P14: dense
- P15: dense
- P16: dense
- P17: dense
- P18: dense
- P19: anchor
- P20: anchor

## pptx_structure
- mode: flat

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters
