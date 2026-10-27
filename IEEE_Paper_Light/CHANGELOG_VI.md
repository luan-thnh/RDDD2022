# Thay đổi bản thảo — 27/10/2026

- Viết lại Abstract, Introduction, Related Work, Methods, Results, Discussion và Conclusion thành một mạch nhất quán: ba YOLO variants, ba seed dùng lại, hai miền train, 18 run, 658 ảnh test / 4.378 ảnh tổng.
- Tính gap theo cùng target; sửa YOLO26 thành 16,91 ± 0,80 pp trên Drone và 42,27 ± 1,28 pp trên MotorBike.
- Thay toàn bộ bảng mean/SD bằng dữ liệu tạo từ metric đã kiểm tra; sửa mAP@50, class AP YOLO26, peak epoch, phiên bản Ultralytics.
- Bỏ các headline 54,67% / 94,3% / 35,3% / 12,24 pp đang bị diễn giải quá phạm vi; định nghĩa riêng relative decline và target asymmetry.
- Bỏ các đoạn convergence lặp, kết luận sai về early stopping, quan hệ variance–model generation và cơ chế camera chưa kiểm tra.
- Thay toàn bộ hình dark/nhầm caption bằng figure nền trắng có thể tái tạo. Bài chính giữ hai figure; validation trajectories nằm trong supplementary. Gap-summary được cung cấp riêng như figure tuỳ chọn, tránh lặp bảng gap đã có trong bài chính. Mỗi hình được dùng chỉ chèn một lần trong bộ bài chính + supplementary.
- Bổ sung YOLO26 citation theo tài liệu chính thức 2026. Bỏ bảng params/FLOPs không có định nghĩa đo tương đương và các citation dùng sai mục đích; không khẳng định SOTA hoặc chưa từng có nghiên cứu tương tự.
- Giữ cả kết quả âm của D40 trên Drone và trường hợp D20 MotorBike của YOLO11 cao hơn YOLO26. Nêu rõ giới hạn ba seed, cùng họ YOLO, size/source confounds, scene audit và metric-level verification.
- Giữ dữ liệu gốc và bản thảo gốc ngoài bộ sửa; không đăng bài, đẩy GitHub hoặc chạy training/inference mới.

## Giới hạn

Đã tái tính từ CSV/JSON và log được cung cấp. Chưa tái chạy inference, audit lại ảnh/XML/split, thực hiện thí nghiệm bổ sung hay tìm literature có hệ thống. Thông tin funding/conflicts/đóng góp tác giả chưa được tự suy diễn; xem README trước khi nộp.
