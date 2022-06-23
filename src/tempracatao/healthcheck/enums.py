from enum import Enum
from typing import List, Tuple


class Status(Enum):
    OK = "ok"
    NOK = "nok"
    WARNING = "warning"

    @classmethod
    def choices(cls) -> List[Tuple[str, str]]:
        return [(i.value, i.value) for i in cls]
