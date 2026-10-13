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
- **Webots:** (Điền phiên bản sau khi cài đặt, ví dụ R2025a hoặc R2023b)

### 2. Quan sát ban đầu về mô phỏng Webots (Scene Tree & e-puck)
*(Ghi lại khi mở world e-puck mẫu trong Webots)*
1. **Robot Node (e-puck):** Đại diện cho toàn bộ thực thể robot trong thế giới vật lý 3D.
2. **Motor Nodes (Bánh xe):** Robot hai bánh vi sai gồm `left wheel motor` và `right wheel motor`. Có thể điều khiển vận tốc (velocity mode) hoặc góc quay (position mode).
3. **Sensor Nodes (Cảm biến khoảng cách / Proximity sensors):** E-puck có 8 cảm biến hồng ngoại (`ps0` đến `ps7`) bố trí xung quanh thân để đo khoảng cách vật cản.
4. **Arena / Obstacles:** Các bức tường và hộp cản trong world để robot tương tác vật lý.
5. **Simulation Time Step:** Webots chạy theo bước thời gian rời rạc `basicTimeStep` (thường là 32ms hoặc 64ms), vòng lặp robot controller phải đồng bộ theo bước này bằng hàm `robot.step(timestep)`.

### 3. Các câu hỏi / Vấn đề cần tìm hiểu tiếp
1. Giá trị trả về từ các cảm biến khoảng cách `ps0` - `ps7` là giá trị thô (raw proximity value) hay là đơn vị mét? Cần hiệu chuẩn (calibration) như thế nào để chuyển đổi sang ngưỡng an toàn?
2. Vận tốc đặt cho motor trong Webots (`setVelocity`) có đơn vị là rad/s hay m/s, và giới hạn tốc độ tối đa của e-puck là bao nhiêu?
3. Khi viết controller bên ngoài bằng Python, làm sao để kết nối với Webots nếu chạy ở chế độ extern controller?

### 4. Checklist hoàn thành Ngày 1
- [x] Khởi tạo Git repo và file `.gitignore`
- [x] Cài đặt môi trường Python 3.10 và các thư viện cần thiết (FastAPI, Uvicorn, WebSockets, Pytest, Pydantic)
- [ ] Cài đặt Webots và mở world mẫu e-puck
- [ ] Bấm Run/Pause/Reset để quan sát hoạt động của robot e-puck
- [ ] Lưu hình ảnh chụp màn hình (screenshot) vào `docs/assets/`
