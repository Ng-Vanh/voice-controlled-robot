# Ngày 2 — Controller Python tối thiểu trong Webots

## Mục tiêu

Cho e-puck chạy thẳng chậm trong 2 giây mô phỏng rồi dừng. Controller nằm ở
`simulator/controllers/day2_controller/day2_controller.py`.

## Chuẩn bị world trong repo

World e-puck mẫu đang nằm trong thư mục cài Webots. Hãy tạo bản sao để không
thay đổi ví dụ gốc:

1. Trong Webots chọn **File → Save World As…**.
2. Lưu world thành `simulator/worlds/e-puck_day2.wbt` trong repo này.
3. Nếu Webots hỏi tạo/copy project, chấp nhận để giữ world trong thư mục
   `simulator/worlds/` và controller trong thư mục ngang hàng
   `simulator/controllers/`.
4. Tạm dừng mô phỏng trước khi thay controller.

## Chọn controller Python

1. Chọn node gốc **E-puck** trong Scene Tree.
2. Trong thuộc tính của node, tìm trường `controller` và đổi giá trị thành
   `day2_controller`.
3. Lưu world bằng **File → Save World**.
4. Nhấn **▶ Run**. Webots sẽ tìm file `day2_controller.py` trong thư mục
   controller cùng tên.

Nếu trường `controller` không hiện, mở node E-puck bằng mũi tên bên trái rồi
chọn lại node gốc robot. Không cần chạy file Python bằng Terminal: Webots phải
chạy controller để cung cấp module `controller` và kết nối thiết bị mô phỏng.

## Quan sát kết quả

- Robot đi thẳng khoảng 2 giây mô phỏng rồi dừng.
- Console không báo `controller not found` hoặc `device not found`.
- Nếu chạy quá xa, sửa `speed` từ `2.0` xuống `1.0`, hoặc giảm
  `run_duration` từ `2.0` xuống `1.0`.

## Đọc code

- `Robot()` kết nối chương trình với robot hiện tại trong Webots.
- `getBasicTimeStep()` lấy chu kỳ mô phỏng; `robot.step(timestep)` tiến mô
  phỏng theo từng bước và cho controller cập nhật.
- `getDevice(...)` lấy đúng motor theo tên thiết bị trong model e-puck.
- `setPosition(float("inf"))` chuyển motor sang điều khiển tốc độ.
- Hai motor cùng tốc độ tạo chuyển động thẳng; tốc độ ở đây là rad/s.
- Thời gian dùng `robot.getTime()`, tức thời gian mô phỏng, không phải đồng hồ
  thực của máy tính.
