# RDD2022 — Scene-Aware Cross-Domain Evaluation

Bản thảo IEEE đánh giá chuyển miền giữa China_Drone và China_MotorBike trên RDD2022, với YOLOv8n, YOLO11n và YOLO26n: ba seed, hai miền huấn luyện, 18 lần train.

## Đọc bài báo

- [Bài chính — PDF 6 trang](IEEE_Paper_Light/main.pdf)
- [Supplementary — PDF 2 trang](IEEE_Paper_Light/supplement.pdf)
- [Hướng dẫn biên dịch và tái tạo hình](IEEE_Paper_Light/README_VI.md)
- [Nhật ký chỉnh sửa](IEEE_Paper_Light/CHANGELOG_VI.md)

Phiên bản này dùng toàn bộ hình nền sáng, đã loại hình và đoạn bị lặp, đồng bộ kết quả YOLO26 và sửa cách tính fixed-target gap, mean/SD và AP từng lớp.

## Nguồn và dữ liệu

Trong `IEEE_Paper_Light/`:

- `main.tex`, `supplement.tex`, `references.bib`: nguồn bài báo.
- `figures/`, `tables/`: hình nền trắng và bảng được tạo từ kết quả đã đối chiếu.
- `data/`: metric full/clean-only, metadata và log huấn luyện của 18 run.
- `scripts/`: script tái tạo bảng/hình, biên dịch và kiểm tra.
- `records/`: hồ sơ kiểm chứng và phạm vi bằng chứng.

Số liệu được tái tính từ các kết quả lưu trữ do tác giả cung cấp; không phải một lần train hoặc inference độc lập mới. Ảnh dữ liệu gốc và trọng số model không nằm trong repository này. Bản thảo trình bày các giới hạn về split, scene audit, ba seed và khác biệt giữa hai nguồn dữ liệu.

## Biên dịch

Cần XeLaTeX, BibTeX và các font/package nêu trong hướng dẫn:

```bash
cd IEEE_Paper_Light
bash scripts/build.sh
```

Để tái tạo bảng và hình từ CSV đã giữ:

```bash
python3 -m pip install -r scripts/requirements.txt
python3 scripts/prepare_manuscript.py
bash scripts/build.sh
python3 scripts/validate_manuscript.py
```

Trước khi nộp, tác giả cần xác nhận thông tin cơ quan, tài trợ, xung đột lợi ích, đóng góp tác giả và yêu cầu của nơi nộp. Không có kết luận SOTA hay bằng chứng nhân quả riêng cho góc camera được khẳng định.
