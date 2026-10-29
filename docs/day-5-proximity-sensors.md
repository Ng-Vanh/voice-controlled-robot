# Ngày 5 — Đọc và phân nhóm cảm biến proximity

## Mục tiêu

Controller `day5_sensor_demo` đọc `ps0`–`ps7`, in từng tín hiệu và mức lớn nhất
theo hướng trước/trái/phải/sau. Robot đi tới chậm để tín hiệu có thể thay đổi
khi có vật ở phía trước; dữ liệu sai hoặc chạm ngưỡng dò thử sẽ khiến robot dừng.

## Cảm biến và đơn vị

E-puck dùng 8 cảm biến hồng ngoại kiểu proximity. Webots trả tín hiệu theo lookup
table của cảm biến (tối đa 4095 trong PROTO R2025a), không phải mét hoặc
centimet. Phản hồi còn phụ thuộc đặc tính vật thể, vì vậy ngưỡng `80` trong demo
chỉ là ngưỡng thử nghiệm được tham khảo từ ví dụ e-puck của Cyberbotics; nó chưa
được hiệu chuẩn thành khoảng cách an toàn.

## Nhóm cảm biến

Robot hướng về phía trước theo trục +x cục bộ. Các nhóm dưới đây theo bố trí
sensor của PROTO e-puck và ví dụ tránh vật cản của Webots. Hai cảm biến chéo
trước được dùng chung trong nhóm trước và một nhóm bên:

| Hướng | Cảm biến |
|---|---|
| Trước | `ps0`, `ps7` |
| Phải | `ps0`, `ps1`, `ps2` |
| Trái | `ps5`, `ps6`, `ps7` |
| Sau | `ps3`, `ps4` |

Giá trị nhóm là tín hiệu lớn nhất trong nhóm, giúp thấy cảm biến nào đang phản
hồi mạnh nhất. Nhóm cảm biến được dùng để quan sát; không dùng để kết luận một
khoảng cách vật lý cụ thể.

## Chạy trong Webots

1. Mở `simulator/worlds/e-puck_day2.wbt`.
2. Chọn robot e-puck và đặt trường `controller` thành `day5_sensor_demo`.
3. Đặt một `WoodenBox` ngay trước hướng nhìn của robot, cách robot một khoảng
   vừa phải để tín hiệu có thể thay đổi khi robot tiến tới.
4. Reset mô phỏng rồi nhấn **▶ Run**.
5. Quan sát Console: các giá trị `ps0`–`ps7` và nhóm hướng được in mỗi 0.25 giây
   mô phỏng. Robot dừng khi tín hiệu trước đạt 80, có dữ liệu lỗi hoặc hết 12
   giây mô phỏng.

Để so sánh, reset và thay đổi khoảng cách/góc của hộp; ghi lại các giá trị thô.
Không đổi ngưỡng thành centimet. Nếu muốn dùng mét, cần cấu hình và hiệu chuẩn
một cảm biến khoảng cách phù hợp riêng.

Chạy kiểm thử phần xử lý số đo từ thư mục repo:

```bash
pytest -q tests/test_epuck_sensor_data.py
```

## Nguồn Webots

- [Tutorial 4: cảm biến e-puck và vòng lặp đọc sensor](https://github.com/cyberbotics/webots/blob/master/docs/guide/tutorial-4-more-about-controllers.md)
- [E-puck PROTO trong Webots R2025a](https://raw.githubusercontent.com/cyberbotics/webots/R2025a/projects/robots/gctronic/e-puck/protos/E-puck.proto)
- [Định nghĩa lookup table của sensor e-puck R2025a](https://raw.githubusercontent.com/cyberbotics/webots/R2025a/projects/robots/gctronic/e-puck/protos/E-puckDistanceSensor.proto)
