# Voice-Controlled Autonomous Robot (Simulation First)

Dự án nghiên cứu & phát triển Robot tự hành điều khiển bằng giọng nói tiếng Việt, tiếp cận theo phương pháp **Mô phỏng trước (Simulation-First)** bằng Webots, trước khi chuyển đổi lên phần cứng (ESP32).

---

## 1. Kiến trúc tổng quan

```
[Microphone / Web UI]
         ↓ (Text/Audio)
[FastAPI Server + WebSocket]
         ↓ (Structured Command JSON)
[Command Parser & Safety Supervisor]
         ↓ (Bridge IPC / Socket)
[Webots Python Controller (e-puck)]
    ├── Differential Drive Kinematics
    └── Obstacle Avoidance FSM (Sensor → Decision → Actuator)
```

---

## 2. Cấu trúc thư mục

```text
voice-controlled-robot/
├── README.md
├── requirements.txt
├── .gitignore
├── docs/
│   ├── architecture.md
│   ├── command-protocol.md
│   ├── test-plan.md
│   ├── learning-notes.md
│   └── assets/
├── simulator/
│   ├── worlds/                    # Tệp .wbt (môi trường mô phỏng)
│   ├── controllers/
│   │   └── robot_controller/      # Controller Python chạy trong Webots
│   └── bridge/                    # Socket/IPC adapter giao tiếp backend
├── robot/
│   ├── interfaces.py             # Interface trừu tượng (phần cứng/mô phỏng)
│   ├── kinematics.py             # Vận tốc bánh vi sai
│   ├── states.py                 # FSM states & transitions
│   ├── obstacle_avoidance.py     # Thuật toán né vật cản thuần logic
│   ├── supervisor.py             # Safety arbitration (STOP > Safe > Move)
│   └── types.py                  # Dataclass Command, Telemetry, Mode
├── ai/
│   ├── command_parser.py         # Chuyển text tiếng Việt sang enum Command
│   └── speech_to_text.py         # STT (faster-whisper)
├── server/
│   └── main.py                   # FastAPI + WebSocket server
├── web/
│   ├── index.html                # Web dashboard điều khiển
│   └── app.js
├── tests/
│   ├── test_command_parser.py
│   ├── test_obstacle_avoidance.py
│   ├── test_supervisor.py
│   └── test_protocol.py
└── logs/
```

---

## 3. Môi trường phát triển

- **Hệ điều hành:** Ubuntu 22.04 LTS (x86_64)
- **Môi trường Python:** Python 3.10 (.venv)
- **Frameworks & Thư viện:** FastAPI, Uvicorn, WebSockets, Pytest, Pydantic
- **Simulator:** Webots (phiên bản khuyến nghị R2023b / R2025a)

### Kích hoạt môi trường ảo:
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### Chạy kiểm thử:
```bash
pytest tests/
```
