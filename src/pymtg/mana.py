from dataclasses import dataclass

from enum import Enum

@dataclass
class ManaData:
    abbreviation: str
    ansi: str

class Mana(ManaData, Enum):
    WHITE = "W", "\\e[0;33m"
    BLUE = "U", "\\e[0;34m"
    BLACK = "B", "\\e[0;35m"
    RED = "R", "\\e[0;31m"
    GREEN = "G", "\\e[0;32m"
    COLORLESS = "C", "\\e[0m"


