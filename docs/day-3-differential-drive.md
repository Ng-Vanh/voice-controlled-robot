# Ngày 3 — Điều khiển chuyển động vi sai

## Mục tiêu

Controller `day2_controller.py` nay có hàm `set_wheel_speeds(left, right)`, giới
hạn tốc độ bánh và lần lượt minh họa tiến, lùi, xoay trái tại chỗ, xoay phải tại
chỗ và dừng. Encoder bánh xe được dùng để in tốc độ góc đo được gần đúng.

## Chạy bài thực hành

1. Mở `simulator/worlds/e-puck_day2.wbt` và xác nhận trường `controller` của
   robot là `day2_controller`.
2. Lưu file Python nếu vừa sửa, rồi reset mô phỏng.
3. Nhấn **▶ Run** và quan sát robot cũng như **Console**.
4. Mỗi chuyển động kéo dài 0.8 giây mô phỏng ở 2 rad/s; sau đó controller gửi
   tốc độ 0 cho cả hai bánh trước khi qua ca tiếp theo.

## Kết quả cần quan sát

| Ca | Bánh trái | Bánh phải | Kết quả mong đợi |
|---|---:|---:|---|
| Tiến | dương | dương | Hai bánh quay cùng chiều, robot tiến |
| Lùi | âm | âm | Hai bánh quay ngược chiều, robot lùi |
| Xoay trái | âm | dương | Robot quay quanh gần tâm thân |
| Xoay phải | dương | âm | Robot quay theo hướng ngược lại |
| Dừng | 0 | 0 | Hai bánh đứng yên |

Console in tốc độ mục tiêu, tốc độ đo gần đúng từ encoder và tốc độ bị giới hạn
nếu giá trị yêu cầu vượt quá `MAX_WHEEL_SPEED`. Giới hạn 6.28 rad/s theo ví dụ
e-puck trong tài liệu Webots; bài thực hành chỉ dùng 2 rad/s.

## Công thức chuyển động

Với bán kính bánh `r`, vận tốc góc bánh trái `ωL`, bánh phải `ωR` và khoảng cách
hai bánh `L`:

```text
v = r(ωR + ωL) / 2
ω = r(ωR - ωL) / L
```

`v` là vận tốc tiến/lùi của tâm robot (m/s), còn `ω` là vận tốc quay thân robot
(rad/s). Hai bánh cùng tốc độ tạo `ω = 0`; hai bánh ngược chiều tạo `v = 0` và
robot xoay tại chỗ.
