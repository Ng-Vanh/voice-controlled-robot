# Ngày 4 — Types, interface robot và parser lệnh

Ngày 4 tách logic lệnh khỏi Webots:

- `robot/types.py` định nghĩa `Command`, `RobotMode` và snapshot `Telemetry`.
- `robot/interfaces.py` khai báo các thao tác robot dùng chung. Interface chưa
  phụ thuộc Webots hay ESP32; `read_distances()` trả số đo thô, chưa giả định đơn vị.
- `ai/command_parser.py` chuẩn hóa chữ hoa/thường, dấu tiếng Việt, dấu câu và
  khoảng trắng trước khi ánh xạ một cụm lệnh hoàn chỉnh sang `Command`.

Các cụm hiện được nhận diện: `đi thẳng`, `tiến lên`, `lùi lại`, `rẽ trái`,
`rẽ phải`, `dừng lại`, `đứng yên`. Cụm không khớp trả `Command.UNKNOWN`; parser
không tự suy đoán lệnh gần giống.

Chạy kiểm thử parser từ thư mục gốc repo:

```bash
pytest -q tests/test_command_parser.py
```

Ví dụ:

```python
from ai.command_parser import parse_command

command = parse_command("  TIẾN lên!!! ")
# Command.MOVE_FORWARD
```
