# Bài báo hoàn thiện từ bản nguồn trước YOLO26

`main.pdf` là bản đọc 7 trang. `main.tex` được chỉnh trực tiếp từ source trước YOLO26 vừa được tác giả cung cấp. Bản gốc nằm trong `provenance/before_yolo26/`; từng thay đổi có trong `qa/baseline_to_final.diff` và `qa/integration_map.csv`.

## Flow được giữ và hoàn thiện

- Giữ tiêu đề, tác giả, hai đoạn mở đầu Introduction, công thức gap, các nhãn và các citation key gốc.
- Giữ Related Work theo Consensus → Trade-off → Gap → This paper; thêm đoạn YOLO evolution theo lượt chỉnh sửa đã có.
- Hoàn thiện phần mở rộng thành bốn RQ, trong đó RQ4 là so sánh ba biến thể YOLO.
- Giữ bảy bảng ngay trong main: số ảnh, số box, mAP@50:95, mAP@50, gap trung bình, gap theo seed, AP từng lớp. Hai bảng số ảnh/box giữ nguyên từ source gốc.
- Giữ phân tích training, Why does performance degrade?, ba nhóm scale/context/class, Comparison with prior work và practical implications/future work.
- Tách Limitations và Threats to Validity theo flow trong conversation; mỗi giới hạn được giữ có mục đích, không chèn lặp vào mọi đoạn.
- Có bốn hình khác nhau, toàn bộ nền trắng: training; fixed-target gaps; class gaps MotorBike; so sánh ba model trên cùng target. Không chèn lại một file training dưới hai tên model.

## Kiểm chứng và skill

Đã sử dụng `latex-paper-en`, `academic-paper-review`, `nature-figure` từ bộ skill tác giả cung cấp, kết hợp skill nghiên cứu của phiên làm việc. Báo cáo tự phản biện nằm trong `qa/academic_review.md`; kết quả chạy công cụ nằm trong `qa/skills/` và `qa/figures/`.

- `qa/verification.json`: kiểm tra số trong từng bảng với metric CSV, bảo toàn các thành phần gốc, negative tests cho duplicate/missing comparator và PDF.
- `qa/figures/`: alignment JSON, collision audits, glyph audits và source data cho hình.
- `qa/skills/abstract.txt`, `logic.txt`, `claim_forward.txt`, `tables.txt`, `figures.txt`: chẩn đoán bản cuối.
- `qa/skills/findings_resolution.md`: giải thích các cảnh báo heuristic và việc xử lý, thay vì tự động sửa bài theo mọi cảnh báo.
- `data/`: 72 dòng metric full/clean-only và 18 training CSVs; không có trọng số hoặc ảnh gốc.

Các số liệu lấy từ kết quả tác giả đã train; không tạo số giả, không train/inference lại và không tuyên bố có thêm thí nghiệm. Những sai lệch gap/SD/class AP và phạm vi của headline cũ được sửa theo dữ liệu. Các cơ chế scale/context/texture vẫn là giả thuyết khi chưa có thí nghiệm tách nguyên nhân.

## Biên dịch và tái tạo

Biên dịch cần XeLaTeX, BibTeX, latexmk, font Liberation Serif/Sans/Mono và Latin Modern Roman Caps. IEEEtran class được giữ kèm. Trên Overleaf chọn XeLaTeX, main document `main.tex`. Bibliography dùng BibTeX numeric style; đổi toolchain này xử lý lỗi font và thiếu Biber, không thay nội dung trích dẫn gốc.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r scripts/requirements.txt
bash scripts/build.sh
```

Để tái tạo toàn bộ bản tích hợp và hình:

```bash
python scripts/finalize_from_baseline.py
python scripts/make_figures.py
bash scripts/build.sh
python scripts/verify_final.py
```

Các bước dùng CPU; không cần GPU hoặc mạng khi đã có các thư viện và TeX. Các script chỉ ghi trong bộ source này, không push GitHub. Có thể chạy lại sau khi sửa lỗi; dữ liệu/baseline không bị reset hoặc xoá. PDF/SVG chứa hình vector có text; PNG và TIFF 600 dpi là bản xuất raster.

## Ranh giới còn lại trước submission

Chưa có venue cụ thể hoặc giới hạn trang được chỉ định. Tác giả cần xác nhận funding, conflicts, author contributions và yêu cầu AI disclosure của nơi nộp. Scene audit, số annotation và các quyết định split giữ theo hồ sơ tác giả; chưa audit độc lập lại ảnh/XML. Việc bibliography key hợp lệ không đồng nghĩa đã kiểm chứng toàn văn hoặc mọi DOI. Đây không phải báo cáo một lần tái lập training/inference mới.
