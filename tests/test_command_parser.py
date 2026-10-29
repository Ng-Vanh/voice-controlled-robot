import pytest

from ai.command_parser import parse_command
from robot.types import Command


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("đi thẳng", Command.MOVE_FORWARD),
        ("tiến lên", Command.MOVE_FORWARD),
        ("  TIẾN   LÊN  ", Command.MOVE_FORWARD),
        ("tiến lên!!!", Command.MOVE_FORWARD),
        ("lùi lại", Command.MOVE_BACKWARD),
        ("LÙI, LẠI!", Command.MOVE_BACKWARD),
        ("rẽ trái", Command.TURN_LEFT),
        ("RẼ, TRÁI!", Command.TURN_LEFT),
        ("rẽ phải", Command.TURN_RIGHT),
        ("DỪNG LẠI.", Command.STOP),
        ("đứng yên", Command.STOP),
        ("đi tới mặt trăng", Command.UNKNOWN),
        ("không đi thẳng", Command.UNKNOWN),
        ("", Command.UNKNOWN),
        (None, Command.UNKNOWN),
    ],
)
def test_parse_command_normalizes_supported_phrases_and_rejects_unknown(
    text, expected
):
    assert parse_command(text) is expected
