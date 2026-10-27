# Bản thảo RDD2022 — phiên bản nền sáng

Đã chỉnh sửa từ bản thảo tác giả cung cấp, đối chiếu đủ 18 archive thực nghiệm và tái tính thống kê. Không thay đổi bản gốc, không train lại và không chạy lại inference.

## File nên mở

- `main.pdf`: bài chính, đủ YOLOv8n / YOLO11n / YOLO26n, hai hình nền trắng.
- `supplement.pdf`: bảng AP từng lớp, gap từng seed, mAP@50, clean-only và một hình nền trắng chứa đường validation của 18 run.
- `main.tex`, `supplement.tex`, `references.bib`: nguồn để chỉnh sửa.
- `figures/`: chỉ bốn hình nền sáng, mỗi hình có PDF vector và PNG 300 dpi. Ba hình được chèn vào bài chính/supplement; hình gap-summary còn lại là tuỳ chọn để tránh lặp lại bảng gap trong bài chính. Không giữ hình dark trong bộ nguồn mới.
- `data/`: metric, metadata và log nguồn phục vụ tái tạo bảng/hình; không có ảnh dữ liệu hoặc trọng số model.
- `CHANGELOG_VI.md`: những thay đổi chính và giới hạn kiểm chứng.

## Biên dịch lại

Đã sử dụng XeLaTeX + BibTeX. Cần TeX Live có `fontspec`, `amsmath`, `booktabs`, `cite`, `hyperref`, `seqsplit`, BibTeX style `ieeetr`; font Liberation Serif/Sans/Mono và Latin Modern Roman Caps. `IEEEtran.cls` được giữ kèm theo từ gói gốc.

```bash
cd IEEE_Paper_Light
bash scripts/build.sh
```

Trên Overleaf: chọn XeLaTeX, đặt main document là `main.tex`. Để biên dịch supplementary, chuyển main document sang `supplement.tex`. Không cần Biber.

## Tái tạo số liệu trình bày và hình

Cần Python 3, numpy, pandas và matplotlib. Chỉ dùng CPU; không cần GPU, ảnh gốc hoặc kết nối mạng nếu dùng các CSV đã giữ trong gói.

```bash
python3 scripts/prepare_manuscript.py
bash scripts/build.sh
python3 scripts/validate_manuscript.py
```

Script đọc CSV/log để tạo `tables/` và `figures/`; không deserialize `.pt` hoặc thực thi mã trong ZIP do tác giả cung cấp. Các file kết quả được tạo lại trong thư mục riêng này. Có thể chạy lại sau khi lỗi biên dịch được khắc phục; không có thao tác reset, xoá checkout, hoặc chỉnh dữ liệu gốc. Không dùng script này để khẳng định đã tái lập training/inference.

## Phần tác giả cần xác nhận trước khi nộp

- Tên cơ quan, thông tin tác giả; funding, competing interests và author contributions theo yêu cầu nơi nộp. Không tự thêm các tuyên bố “không tài trợ/không xung đột” khi chưa được tác giả xác nhận.
- Các chi tiết audit ảnh/split, số bbox và việc researcher kiểm tra scene-review được giữ theo hồ sơ bản thảo gốc; chưa kiểm tra độc lập với ảnh/XML gốc.
- Nơi nộp và giới hạn trang chưa được chỉ định; đây là bản IEEE conference A4. Áp dụng template, giới hạn trang và AI disclosure cụ thể khi chọn venue.
- Network của phiên làm việc chặn truy cập trực tiếp arXiv, PMLR và MDPI. Các mô tả literature được thu hẹp theo abstract/citation/README của dự án chính chủ đã mở; không tuyên bố đã đọc lại toàn văn mọi paper hoặc làm novelty audit hệ thống. Nhật ký truy cập nằm trong `literature/`.

Các mục này không ngăn việc sử dụng bản PDF đã biên dịch để tác giả đọc và chỉnh tiếp; chúng là thông tin cần chốt cho submission thực tế.
