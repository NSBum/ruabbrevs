import re
from typing import Tuple, Optional


def parse_line(line: str) -> Optional[Tuple]:
    comps = line.split('||')
    return comps
