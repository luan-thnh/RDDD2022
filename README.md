# RDD2022 — Scene-Aware Cross-Domain Evaluation

**Bản hiện tại nằm trong [`IEEE_Paper/`](IEEE_Paper/).** Bản này được hoàn thiện trực tiếp từ source trước YOLO26 do tác giả cung cấp, theo flow chỉnh sửa đã thống nhất: bốn RQ, ba biến thể YOLO, 18 lần train, bảy bảng trong main và bốn hình nền sáng.

## Đọc bản hiện tại

- [Bài báo hoàn thiện — PDF 7 trang](IEEE_Paper/main.pdf)
- [Source LaTeX](IEEE_Paper/main.tex)
- [Hướng dẫn biên dịch và tái tạo](IEEE_Paper/README_VI.md)
- [Source gốc trước YOLO26 được giữ nguyên](IEEE_Paper/provenance/before_yolo26/main.tex)
- [Diff từng thay đổi từ bản gốc](IEEE_Paper/qa/baseline_to_final.diff)
- [Đối chiếu với flow chỉnh sửa](IEEE_Paper/qa/flow_contract.csv)
- [Báo cáo tự phản biện theo skill](IEEE_Paper/qa/academic_review.md)
- [Kết quả kiểm chứng số liệu và source](IEEE_Paper/qa/verification.json)

Giữ mạch Consensus → Trade-off → Gap → This paper, phân tích training, giải thích scale/context/class và so sánh nghiên cứu trước. Hoàn thiện thêm YOLO evolution, RQ4 và phần Limitations/Threats theo flow đang viết dở. Các số gap, SD và class AP được sửa theo dữ liệu đã đối chiếu.

## Nguồn và dữ liệu

Trong `IEEE_Paper/`:

- `main.tex`, `references.bib`, `main.pdf`: nguồn và bản biên dịch hiện tại.
- `figures/`: bốn hình light, có PDF/SVG vector và PNG/TIFF 600 dpi.
- `data/`: 72 metric rows full/clean-only, metadata và 18 training CSVs.
- `scripts/`: tái tạo bản tích hợp, hình, biên dịch và kiểm chứng.
- `qa/`: các kiểm tra LaTeX, figure geometry, claim–evidence, source diff và kết quả phản biện.
- `provenance/`, `records/`: bản nền được bảo toàn, hồ sơ thay đổi và ranh giới bằng chứng.

Số liệu được tái tính từ các kết quả lưu trữ tác giả cung cấp; không có lần train/inference độc lập mới. Ảnh gốc và trọng số model không nằm trong repository. Các giới hạn của scene audit, source-size confounds, ba seed và phạm vi một họ detector được trình bày trong bài.

## Biên dịch

Cần XeLaTeX, BibTeX, latexmk và các font/package nêu trong hướng dẫn. Trên Overleaf chọn XeLaTeX và `main.tex`.

```bash
cd IEEE_Paper
bash scripts/build.sh
```

Tái tạo bảng/hình trong venv:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r scripts/requirements.txt
python scripts/finalize_from_baseline.py
python scripts/make_figures.py
bash scripts/build.sh
python scripts/verify_final.py
```

Tác giả cần xác nhận các declarations và yêu cầu của venue trước submission. Các kiểm tra theo skill không phải peer review của hội nghị hoặc chứng nhận acceptance.

## Bản trước để đối chiếu

[`IEEE_Paper_Light/`](IEEE_Paper_Light/) là bản chỉnh sửa trước đây, được giữ để đối chiếu lịch sử. Dùng PDF và source trong **`IEEE_Paper/`** cho bản hiện tại; các bảng chi tiết hiện đã nằm trong main.
