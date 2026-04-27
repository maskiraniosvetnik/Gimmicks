import re
from pathlib import Path
from config import PATTERNS

compiled = [re.compile(p, re.IGNORECASE) for p in PATTERNS]

def is_target(name: str) -> bool:
    return any(p.match(name) for p in compiled)

def scan(paths):
    files = []
    for base in paths:
        if not base.exists():
            continue
        for item in base.iterdir():
            if item.is_file() and is_target(item.name):
                files.append(item)
    return files