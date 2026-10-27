# Kiểm tra bản nâng cấp bằng PPT Master

- Đầu vào: bộ slide tại commit `1ad4e80`; giữ 20 slide / 8 phần và thứ tự gốc.
- Thiết kế: bìa bất đối xứng, tiêu đề serif Georgia, nội dung Arial, nền trắng, xanh navy–teal, nhấn YOLO26n bằng màu amber; bảng mở, ảnh lớn và chart trên cùng thang đo.
- Từng trang có cùng tập ký tự (bỏ khoảng trắng) với bản gốc; công cụ `beautify_inventory.py --verify` xác nhận mọi chuỗi nguồn ở đúng trang. Không thêm hoặc sửa kết quả nghiên cứu.
- 20/20 ghi chú giữ nguyên; PowerPoint ZIP toàn vẹn; PDF đủ 20 trang, không mất token chữ khi xuất.
- SVG: kiểm tra sau trang 5, sau đủ 20 trang và sau sửa; bản cuối **0 error, 0 warning**. Native PPTX postflight: `passed`, không có warning category.
- Biểu đồ: kiểm tra 12 thanh mean và vạch SD ở slide 13, 18 điểm seed ở slide 14, 12 thanh theo lớp ở slide 15. Log slide 12 vẽ lại từ đủ 150 epoch của CSV, không làm mượt.
- Đã rà contact sheet và các trang lớn. Sửa vùng bao mũi tên slide 9, chiều cao chú giải slide 14, đồng bộ trục 60 và một sai số hình học 0,192 px ở slide 15.
- PDF thử có xuống dòng thêm do font thay thế trong LibreOffice. Đã bổ sung 15% khoảng dư vô hình cho khung chữ nhiều dòng trong bản exporter cục bộ; không đổi cỡ chữ, baseline SVG hoặc nội dung. Xuất lại, rà ảnh và đối chiếu chữ đạt yêu cầu. Chi tiết ở `source/README.md`.

Nguồn SVG chứa toàn bộ thiết kế; bản PPTX xuất thành chữ, đường, hình và nhóm DrawingML có thể chỉnh sửa. Chart và bảng hiện là các phần tử chỉnh sửa riêng; PNG log cùng ảnh chứng cứ giữ dạng raster. Không chạy lại training/inference. Ảnh GT/pred vẫn được ghi rõ là validation của miền nguồn.
