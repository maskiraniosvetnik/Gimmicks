import json
import os

ARCHIVE_FILE = "artifacts.json"


def load_archive():
    if not os.path.exists(ARCHIVE_FILE):
        return []
    with open(ARCHIVE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_archive(data):
    with open(ARCHIVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def add_to_archive(exhibit):
    archive = load_archive()
    archive.append(exhibit)
    save_archive(archive)
