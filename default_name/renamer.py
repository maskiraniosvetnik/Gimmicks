from pathlib import Path
from levels import get_level, pick_name

def rename_files(files, dry_run=False):
    count = len(files)
    level = get_level(count)

    log = []

    for i, f in enumerate(files):
        new_name = pick_name(level, i + 1) + f.suffix
        new_path = f.with_name(new_name)

        entry = (f.name, new_name)

        if dry_run:
            print(f"[DRY] {f.name} → {new_name}")
        else:
            try:
                f.rename(new_path)
                print(f"[REN] {f.name} → {new_name}")
            except Exception as e:
                print(f"[ERR] {f.name}: {e}")

        log.append(entry)

    return level, log