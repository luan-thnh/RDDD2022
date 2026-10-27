# 01_cover

Bài trình bày bám theo cấu trúc 20 slide, 8 phần do nhóm cung cấp và cập nhật từ bản paper đã bổ sung YOLO26n. Câu hỏi trung tâm là khi chuyển giữa ảnh thu bằng Drone và MotorBike, độ chính xác thay đổi bao nhiêu trên cùng một tập ảnh đích. Đây là nghiên cứu đánh giá thực nghiệm, với ba biến thể YOLO và ba seed; chưa đề xuất kiến trúc mới. Sơ đồ bìa biểu diễn hai miền và thiết kế đánh giá hai chiều; bằng chứng ảnh thực tế và số liệu được trình bày ở các slide tiếp theo.

---

# 02_agenda

Bố cục giữ tám phần như tài liệu cau_truc.md. Phần đầu đặt vấn đề triển khai và xác định câu hỏi. Tiếp theo là dữ liệu, giao thức so sánh trên cùng tập đích, mô hình và cách huấn luyện. Phần kết quả tách hiệu năng tổng thể, độ ổn định qua seed, khác biệt theo lớp, kiểm tra độ nhạy và ảnh minh họa. Cuối cùng là giới hạn của bằng chứng và các đối chứng cần bổ sung. Các đoạn về Czech và India trong cấu trúc cũ được chuyển thành hướng nghiên cứu, vì bộ kết quả hiện tại chỉ xác nhận hai miền Drone và MotorBike.

---

# 03_context

Quan sát hai ảnh minh họa: Drone nhìn từ trên xuống, còn MotorBike nhìn dọc mặt đường. Bối cảnh cảnh quan, tỷ lệ và hình dạng biểu kiến có thể khác nhau. Đây chỉ là mô tả từ ví dụ, chưa phải kết quả đo riêng về độ sáng, kích thước hộp hay nguyên nhân suy giảm. Trong thiết kế hiện tại, góc nhìn đồng thời thay đổi với cảnh và cỡ tập huấn luyện. Vì vậy câu hỏi phù hợp là mức chênh lệch gắn với lựa chọn miền huấn luyện, được đo trên tập đích cố định. Chưa diễn giải chênh lệch đó thành tác động nhân quả của độ cao hoặc góc camera.

---

# 04_questions

Bốn RQ được giữ đúng theo paper hiện tại. RQ1 đo gap riêng trên Drone Test và MotorBike Test. RQ2 kiểm tra tính nhất quán qua ba seed ghép cặp và ba biến thể. RQ3 phân tích AP từng lớp để tránh kết luận chỉ dựa trên mAP tổng. RQ4 là phần bổ sung YOLO26n: điểm tuyệt đối có thể tăng nhưng mức phụ thuộc miền chưa chắc giảm. Giả thuyết cần kiểm chứng là lợi thế của mô hình huấn luyện trên miền đích khi hai mô hình cùng được chấm trên các ảnh đích giống hệt nhau. Không lấy hiệu năng trên hai quần thể test khác nhau để định nghĩa gap chính.

---

# 05_objectives

Mục tiêu là xây dựng một so sánh mô tả có thể kiểm tra lại từ các kết quả lưu trữ. Chúng ta dùng hai miền thu nhận tại China của RDD2022, ba biến thể nano và ba seed. Mỗi model được fine-tune độc lập trên một miền, sau đó được chấm trên cả Drone Test và MotorBike Test. Phần mở rộng YOLO26n giữ cùng giao thức để xem kết luận trước đó có còn lặp lại. Nghiên cứu hiện tại không phải so sánh mọi họ detector, chưa thử thích nghi miền, và chưa cung cấp đánh giá được xác nhận trên Czech hoặc India.

---

# 06_dataset

RDD2022 là nguồn dữ liệu gốc; các con số trên slide thuộc tập con khóa v4.1 của nghiên cứu. Drone có 1.680 ảnh train, 360 validation và 361 test. MotorBike có 1.383 train, 297 validation và 297 test. Tổng cộng 4.378 ảnh, trong đó 658 ảnh test. Chia tập được thực hiện theo nhóm cảnh dựa trên các liên kết được nhận diện trong đợt rà soát, nhằm giảm trùng cảnh giữa các phân vùng. Quy tắc này bảo vệ các liên kết đã phát hiện, chưa chứng minh loại bỏ hết mọi trùng cảnh tiềm ẩn. Chênh lệch cỡ tập train giữa hai miền vẫn là yếu tố gây nhiễu cần đối chứng.

---

# 07_classes

Bốn nhãn đích là D00 nứt dọc, D10 nứt ngang, D20 nứt da cá sấu và D40 ổ gà. Đây là các crop từ mosaic nhãn validation lưu trong gói thực nghiệm YOLO11n seed 13, không phải ảnh mới được gán nhãn lại. Riêng D40 phóng vùng có nhãn để nhìn rõ ví dụ; không dùng hình này để suy ra phân bố kích thước. Crop D20 vẫn giữ nhãn D00 xuất hiện cùng ảnh. Các nhãn ngoài bốn lớp như Repair và Block crack đã bị lọc, không ánh xạ sang D40. Chúng ta vẫn giữ D40 trong metric chính dù số lượng hỗ trợ ít và kết quả có thể đảo chiều.

---

# 08_distribution

Bảng này đếm hộp nhãn, không phải số ảnh. Drone Test có 214 hộp D00, 189 D10, 44 D20 và 17 D40; MotorBike lần lượt có 403, 165, 96 và 35. Điểm cần nhấn mạnh là D40 trên Drone chỉ có 17 hộp trong 9 ảnh, nhiều ảnh gắn với một nhóm cảnh. Do đó thay đổi AP ở lớp này có thể bị chi phối bởi ít phát hiện. Slide không đưa thống kê kích thước hộp, độ sáng hoặc độ phân giải theo miền vì nguồn hiện tại chưa đo những phân bố đó. Các yếu tố này chỉ là giả thuyết cho phân tích tiếp theo, chưa phải kết quả đã xác nhận.

---

# 09_protocol

Giao thức bắt đầu bằng rà soát liên kết cảnh và khóa phân vùng. Rà soát cũ ghi 735 cặp ưu tiên cao: 629 cùng cảnh, 93 khác cảnh và 13 chưa chắc chắn; số liệu này do tác giả báo cáo, chưa được tái kiểm tra độc lập ở bước làm slide. Mỗi biến thể được fine-tune trên Drone hoặc MotorBike với ba seed. Checkpoint được chọn dựa vào validation miền nguồn, không dùng test để chọn. Bảng 2×2 là trọng tâm: trong cột Drone Test, so D→D với M→D; trong cột MotorBike Test, so M→M với D→M. Cách so sánh này giữ nguyên quần thể test trong từng phép tính gap.

---

# 10_metric

Ký hiệu X là miền còn lại, Y là miền đích đang xét. Với mỗi seed, lấy mAP của model huấn luyện trên Y trừ mAP của model huấn luyện trên X, cùng đánh giá trên Test Y. Sau đó tính trung bình và độ lệch chuẩn mẫu của ba gap ghép cặp. Vì mAP được báo theo phần trăm, phép trừ có đơn vị điểm phần trăm, viết tắt pp. Giảm tương đối phần trăm cần chia cho baseline huấn luyện trên đích; nếu tính từ các mean phải ghi rõ đó là tỷ số của mean. SD mô tả độ biến động giữa ba seed, không phải khoảng tin cậy và chưa đo bất định ở cấp cảnh. mAP@50 được giữ trong paper như chỉ số bổ sung.

---

# 11_models

Ba model là YOLO11n, YOLOv8n và YOLO26n, đều khởi tạo từ trọng số COCO. Cấu hình fine-tune tường minh được giữ chung: 150 epoch, ảnh 640, batch 8, SGD với lr 0,01, momentum 0,937, weight decay 0,0005, warmup 3 epoch. Các phép mosaic, mixup và HSV bị tắt; translate 0,05, scale 0,15 và fliplr 0,5 vẫn bật. Patience bằng 0 nên không gọi đây là early stopping. Ba seed giống nhau được dùng lại ở từng model và miền, không phải chín seed độc lập. Đây là so sánh ba biến thể cùng họ dưới cấu hình đã ghi, chưa bao quát các detector hoặc chế độ tối ưu khác.

---

# 12_training

Đây là ví dụ đại diện YOLO11n huấn luyện trên Drone, ba seed 13, 37 và 71. Hai biểu đồ loss là tổng ba thành phần được ghi: box, cls và dfl. Biểu đồ phải là mAP@50:95 trên validation, không phải trên test. Các đường được vẽ trực tiếp từ CSV, không làm mượt. Điểm tròn đánh dấu mAP validation lớn nhất tại epoch 110, 92 và 111. Tất cả 18 log của nghiên cứu có 150 epoch; trên toàn bộ các lượt, vị trí đỉnh validation nằm trong khoảng 63 đến 133. Việc có đỉnh trước khi kết thúc không tự chứng minh hội tụ toàn cục hay cho phép đổi ngân sách đã dùng.

---

# 13_performance

Mỗi panel cố định một tập test. Thanh xanh đậm là model được huấn luyện trên chính miền đích; thanh nhạt là model học từ miền còn lại. Vạch sai số là SD qua ba seed, không phải CI. Trên Drone, ba mean cùng miền là 22,39; 21,41; 24,49 phần trăm, còn mean xuyên miền là 7,25; 6,55; 7,58. Trên MotorBike, mean cùng miền là 53,08; 51,25; 54,75, còn xuyên miền là 10,15; 10,01; 12,48. YOLO26n nâng mean cùng miền so với YOLOv8n thêm 3,08 và 3,50 pp. Đây là khác biệt mô tả; chưa có kiểm định để kết luận ưu thế có ý nghĩa thống kê.

---

# 14_seed_gap

Biểu đồ hiển thị đủ 18 gap ghép cặp. Mỗi hàng có ba điểm ứng với seed 13, 37 và 71, đoạn nối chỉ biểu diễn khoảng giá trị, không phải CI. Mean gap trên Drone lần lượt là 15,13 ± 3,85; 14,86 ± 1,25; 16,91 ± 0,80 pp. Trên MotorBike là 42,94 ± 0,52; 41,24 ± 1,04; 42,27 ± 1,28 pp. Tất cả điểm đều nằm phía dương. Chênh lệch giữa hai mean gap đích đạt 25,36 đến 27,80 pp tùy model. Đây là bất đối xứng gắn với miền trong dữ liệu hiện tại, chưa cô lập tác động góc nhìn hoặc cỡ tập nguồn.

---

# 15_class_gap

Trên MotorBike Test, D20 có lợi thế huấn luyện đúng miền rất lớn: 57,72 pp với YOLO11n, 53,21 với YOLOv8n và 56,45 với YOLO26n. Tỷ lệ giảm so với AP của baseline huấn luyện trên MotorBike lần lượt khoảng 98,30%, 96,14% và 97,34%. Tuy nhiên, xu hướng tổng thể không đúng cho mọi lớp trên mọi đích. Với D40 của Drone Test, mean gap là âm: −6,61; −9,74; −1,95 pp. Kết quả này được giữ nguyên, không sửa nhãn hoặc bỏ lớp để cải thiện metric. Vì lớp D40 trên Drone có ít hộp và ít cảnh, chưa giải thích đảo chiều bằng một cơ chế thị giác hay đặc tính kiến trúc cụ thể.

---

# 16_sensitivity

Phần đánh giá mở rộng của cấu trúc cũ được cập nhật thành kiểm tra độ nhạy có bằng chứng hiện tại, không dùng kết quả Czech hoặc India chưa xác nhận. Clean-only giữ các ảnh không có annotation ngoài bốn lớp mục tiêu; không có nghĩa mỗi ảnh chứa đủ bốn lớp. Số ảnh còn lại là 273 Drone và 271 MotorBike. Bảng so mean gap full và clean-only; cả 18 gap clean-only theo seed vẫn dương. Với YOLO26n, mean gap clean-only là 16,59 pp trên Drone và 42,60 pp trên MotorBike. Vì quần thể ảnh đã thay đổi, không diễn giải chênh lệch full/clean như ước lượng riêng của ảnh hưởng nhãn ngoài phạm vi.

---

# 17_qualitative

Hai panel lấy từ cùng ảnh China_MotorBike_001773.jpg trong mosaic validation của YOLO11n huấn luyện trên MotorBike, seed 13. Panel trái là nhãn thật; panel phải là dự đoán và điểm tin cậy do bản lưu gốc hiển thị. Có thể quan sát sự khác nhau giữa khung/nhãn được vẽ ở vùng nứt phía dưới, nhưng chưa tổng quát thành tỷ lệ lỗi hoặc nguyên nhân suy giảm. Không gọi đây là minh họa test xuyên miền. Bộ lưu trữ hiện tại chưa cung cấp một audit FP/FN độc lập theo từng ảnh test và chưa chạy lại suy luận từ checkpoint trong lần phân tích này. Mục đích slide là cho thấy dạng đầu ra và sự cần thiết của bước kiểm chứng trực quan tiếp theo.

---

# 18_limitations

Các kết quả là liên hệ mô tả giữa miền huấn luyện và hiệu năng. Cỡ tập train, cảnh, hình học thu nhận và phân bố lớp cùng biến đổi nên chưa tách tác động riêng. Ba seed và ba biến thể nano cho kiểm tra lặp lại trong phạm vi hẹp, chưa chứng minh tổng quát cho mọi detector. Rà soát cảnh chỉ kiểm soát các liên kết đã nhận diện. Một số ảnh MotorBike đã được gặp khi phân tích thăm dò trước khi khóa split, nên không tuyên bố holdout hoàn toàn chưa từng được xem. Phân tích hiện tại kiểm tra và tính lại bảng metric đã lưu, chưa độc lập chạy lại mọi checkpoint trên ảnh gốc hoặc replay audit XML. D40 hiếm và việc clean-only đổi quần thể ảnh cũng hạn chế diễn giải.

---

# 19_conclusions

Kết luận thứ nhất: trên tập con scene-aware khóa, model được huấn luyện đúng miền đích có lợi thế tổng thể trong cả 18 so sánh. Mean gap trên Drone là 14,86–16,91 pp, trên MotorBike là 41,24–42,94 pp. Kết luận thứ hai: ba model lặp lại xu hướng nhưng từng lớp có hành vi khác nhau, nổi bật là D20 trên MotorBike và đảo chiều D40 hiếm trên Drone. Kết luận thứ ba: YOLO26n nâng mean độ chính xác cùng miền so với YOLOv8n nhưng chưa giải quyết được gap. Đóng góp chính là một giao thức có thể kiểm tra từ kết quả theo seed trên cùng tập đích, không tuyên bố kiến trúc mới hay chứng minh nguyên nhân góc nhìn.

---

# 20_next_steps

Ưu tiên đầu tiên là kiểm chứng độc lập: chạy lại suy luận từ checkpoint trên test gốc, lưu đầu ra từng ảnh và kiểm tra lỗi, sau đó ước lượng bất định theo cảnh. Thứ hai là cân bằng cỡ tập huấn luyện để kiểm tra vai trò lượng dữ liệu. Thu ảnh ghép cặp trên cùng đoạn đường bằng các thiết bị hoặc góc nhìn khác nhau sẽ giúp tách hình học thu nhận. Thứ ba là mở rộng Czech, India hoặc dữ liệu ngoài RDD2022, nhưng cần audit ontology nhãn trước khi gộp vào bằng chứng. Cuối cùng mới thử huấn luyện đa miền hoặc thích nghi miền và đánh giá theo đúng split, seed và metric đã khóa. Đây là hướng đề xuất, chưa phải thực nghiệm đã hoàn tất.
