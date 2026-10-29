"""Map simple Vietnamese phrases to high-level robot commands."""

import re
import unicodedata

from robot.types import Command


_ALIASES = {
    "di thang": Command.MOVE_FORWARD,
    "tien len": Command.MOVE_FORWARD,
    "lui lai": Command.MOVE_BACKWARD,
    "re trai": Command.TURN_LEFT,
    "re phai": Command.TURN_RIGHT,
    "dung lai": Command.STOP,
    "dung yen": Command.STOP,
}


def _normalize(text: str) -> str:
    text = text.lower().replace("đ", "d")
    text = unicodedata.normalize("NFD", text)
    text = "".join(char for char in text if not unicodedata.combining(char))
    text = re.sub(r"[^\w\s]", " ", text)
    return " ".join(text.split())


def parse_command(text: str) -> Command:
    """Parse a complete phrase; unrecognized input always maps to UNKNOWN."""
    if not isinstance(text, str):
        return Command.UNKNOWN
    return _ALIASES.get(_normalize(text), Command.UNKNOWN)
