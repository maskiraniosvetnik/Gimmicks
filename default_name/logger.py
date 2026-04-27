from datetime import datetime
from pathlib import Path

LOG_FILE = Path.home() / ".rename_gimmick_log.txt"

def write_log(level, entries):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n=== SESSION {datetime.now()} | LEVEL {level} ===\n")
        for old, new in entries:
            f.write(f"{old} -> {new}\n")