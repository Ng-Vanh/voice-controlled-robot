# Capability Map: Voice-Controlled Autonomous Robot

This map decomposes the simulation-first MVP into independently testable capabilities.
The module IDs are stable and are used to index the specifications and implementation
work that follow.

| Module ID | Responsibility | Depends on |
|---|---|---|
| robot-safety | Safety arbitration, movement modes, timeouts, emergency stop, and obstacle-avoidance decisions | — |
| command-protocol | Typed command and telemetry schemas, validation, serialization, and error semantics | robot-safety |
| simulator-adapter | Webots controller, sensors, motors, and bridge transport | robot-safety, command-protocol |
| command-input | Vietnamese text intent parsing and speech-to-text integration boundary | command-protocol |
| control-server | FastAPI/WebSocket orchestration, command routing, telemetry fan-out, and lifecycle handling | command-protocol, simulator-adapter, command-input |
| web-dashboard | Manual controls, emergency stop, mode selection, telemetry display, and command feedback | command-protocol, control-server |

## Build order

1. `robot-safety`
2. `command-protocol`
3. `simulator-adapter` and `command-input` (parallel after their dependencies)
4. `control-server`
5. `web-dashboard`
6. End-to-end integration across all modules

## Boundary rules

- The `robot-safety` module must remain independent of Webots, FastAPI, browser APIs,
  and network transport so it can be unit tested in isolation.
- Webots-specific APIs belong only to `simulator-adapter`.
- `command-protocol` owns the contract between modules; consumers must not invent
  alternate command or telemetry shapes.
- Speech recognition is an input adapter. Safety decisions must not depend on the
  availability of a speech-to-text service.
- The server may request movement, but the robot controller remains the final safety
  authority for obstacle detection, emergency stop, and control timeouts.
