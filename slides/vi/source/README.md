# Nguồn thiết kế slide tiếng Việt

Nguồn tạo bằng [PPT Master 6.7.3](https://github.com/hugohe3/ppt-master), workflow Generate → Beautify, Default; tác giả giao quyền tự chọn thiết kế trong chat.

- `svg_output/`: 20 trang SVG đầy đủ, có thể chỉnh sửa trực tiếp. Mọi chữ, hình, ảnh và biểu đồ đều hiện diện trong SVG hoặc được tham chiếu bởi nó.
- `images/`: 9 ảnh được dùng; ảnh validation giữ nguyên, `training_redrawn.png` vẽ lại từ log trong `IEEE_Paper/data/training_logs/`.
- `notes/`: ghi chú gốc, một file cho mỗi trang và `total.md`.
- `design_spec.md`, `spec_lock.md`: quy chuẩn thiết kế và nội dung đã khóa.
- `analysis/`: nội dung gốc và ba hướng đã cân nhắc.
- `validation/`: kiểm tra tọa độ chart và đánh giá cách dùng hình thức trình bày.

Bản PowerPoint đầu vào có trong lịch sử Git ở commit `1ad4e80`. Không sao chép toàn bộ bộ skill vào repo. Để xuất lại cần bản PPT Master tương ứng; dùng đường dẫn tuyệt đối đến thư mục skill và thư mục nguồn này. Chạy quality checker trước, tách notes, finalize SVG rồi `svg_to_pptx.py` theo hướng dẫn của skill.

Bản xuất hiện tại dùng native DrawingML cho chữ/hình và các phần tử chart/table, không bật thay thế bằng đối tượng Chart/Table. Một số công cụ như LibreOffice có thể tự ngắt dòng dù DrawingML đặt `wrap=none`; bản exporter dùng trong lần này đã thêm 15% khoảng dư vào chiều rộng khung nhiều dòng. Thay đổi duy nhất ở `scripts/svg_to_pptx/drawingml/elements.py`: sau dòng `text_width = max(visual_line_widths) if visual_line_widths else 0.0`, thêm `text_width *= 1.15`. Giữ nguyên SVG, cỡ chữ và các dòng xuống hàng đã định. Khi dùng exporter chưa sửa, cần rà lại PDF ở các tiêu đề nhiều dòng.

Ghi nhận công cụ: PPT Master, Copyright (c) 2025–2026 Hugo He, giấy phép MIT. Nguồn ảnh và dữ liệu nghiên cứu theo chú thích trong slide; không có ảnh AI hoặc kết quả khoa học mới.
