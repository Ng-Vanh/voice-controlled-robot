# Nhật ký học tập & Quan sát dự án Robot

---

## Ngày 1 — Làm quen với simulator và chạy ví dụ có sẵn

- **Ngày thực hiện:** 13/10/2026
- **Mục tiêu:** Cài đặt môi trường, chạy thử Webots, làm quen với robot mẫu e-puck và quan sát Scene Tree.

### 1. Thông số môi trường phần cứng & phần mềm
- **Hệ điều hành:** Ubuntu 22.04.1 LTS (Linux kernel 6.8.0-138-generic)
- **Kiến trúc CPU:** x86_64 — Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz (8 cores)
- **RAM:** 16 GB (15 GiB thực tế)
- **GPU:** Intel HD Graphics 530 (VGA compatible)
- **Môi trường Python:** Python 3.10.20 (venv tại `.venv`)
- **Phiên bản Pytest:** pytest 9.1.1
- **Webots:** Webots R2025a (APT package: webots 2025a, đường dẫn `/usr/local/webots`)

### 2. Quan sát ban đầu về mô phỏng Webots (Scene Tree & e-puck)
*(Ghi lại khi mở world e-puck mẫu trong Webots)*
1. **Robot Node (`E-puck` PROTO):** Đại diện cho toàn bộ thực thể robot trong thế giới vật lý 3D, chứa các thông số vật lý (mass, translation, rotation).
2. **Motor Nodes (Bánh xe):** Robot hai bánh vi sai gồm:
   - `left wheel motor` (gắn ở bánh trái)
   - `right wheel motor` (gắn ở bánh phải)
   - Được điều khiển ở chế độ vận tốc (Velocity mode) bằng cách đặt position vô hạn `setPosition(float('inf'))` rồi gọi `setVelocity(rad/s)`.
3. **Sensor Nodes (Cảm biến khoảng cách / Proximity sensors):** E-puck tích hợp 8 cảm biến hồng ngoại đặt tên từ `ps0` đến `ps7` bố trí xung quanh thân (phía trước, hai bên chéo và phía sau) để phát hiện vật thể ở cự ly gần.
4. **Arena / Obstacles:** Sàn đấu (`RectangleArena`) và các khối hộp vật cản để robot tương tác vật lý.
5. **Simulation Time Step:** Webots chạy theo chu kỳ `basicTimeStep` (thường là 32ms hoặc 64ms trong world info), controller phải đồng bộ theo bước này bằng hàm `robot.step(timestep)`.

### 3. Các câu hỏi / Vấn đề cần tìm hiểu tiếp
1. Giá trị trả về từ các cảm biến khoảng cách `ps0` - `ps7` là giá trị thô (raw proximity value: càng gần vật cản giá trị càng cao, tối đa ~4000) hay đơn vị mét? Cần hiệu chuẩn (calibration) như thế nào để chuyển đổi sang ngưỡng an toàn?
2. Vận tốc góc tối đa đặt cho motor e-puck trong Webots là bao nhiêu rad/s (thường là ~6.28 rad/s tương ứng 1 vòng/giây)?
3. Vòng lặp điều khiển ngày 2 sẽ kết nối với Webots như thế nào: chạy Internal controller trong Webots hay chạy External Python controller từ ngoài terminal?

### 4. Checklist hoàn thành Ngày 1
- [x] Khởi tạo Git repo và file `.gitignore`
- [x] Cài đặt môi trường Python 3.10 và các thư viện cần thiết (FastAPI, Uvicorn, WebSockets, Pytest, Pydantic)
- [x] Cài đặt Webots (bản R2025a) và mở world mẫu e-puck (`e-puck.wbt`)
- [x] Bấm Run/Pause/Reset để quan sát hoạt động của robot e-puck
- [x] Phân tích Scene Tree và ghi nhận 5 quan sát + 3 câu hỏi vào nhật ký
- [ ] Chụp screenshot robot lưu vào `docs/assets/` (tùy chọn)
