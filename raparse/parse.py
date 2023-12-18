import re
from typing import Tuple, Optional, List
from rautils.textutils import *
from constants import AbbrevIdx


def parse_line(line: str) -> Optional[Tuple]:
    comps = line.split('||')
    parsed_comps = []
    for idx, comp in enumerate(comps):
        if idx == AbbrevIdx.order.value:
            # order in list
            parsed_comps.append(extract_number(comp))
        elif idx == AbbrevIdx.abbrev.value:
            parsed_comps.append(extract_template_name(comp))
        elif idx == AbbrevIdx.expanded.value or idx == AbbrevIdx.type.value:
            # expansion of abbreviation or type
            parsed_comps.append(extract_wikilinks(comp))
        else:
            break
    return tuple(parsed_comps)


def parse_text(text: list) -> Optional[List[Tuple]]:
    abbrevs = []
    for line in text:
        if line.startswith('|') and any(char.isdigit() for char in line[1:]):
            # this is an abbreviation line
            a = parse_line(line)
            abbrevs.append(a) if a else next
    return abbrevs

