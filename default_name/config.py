from pathlib import Path

USER_SCOPES = [
    Path.home() / "Desktop",
    Path.home() / "Downloads",
    Path.home() / "Documents",
    Path.home() / "Pictures",
]

PATTERNS = [
    r"^New Folder(\s\(\d+\))?$",
    r"^Untitled.*",
    r"^file(\s\(\d+\))?$",
    r"^Document\d*$",
    r"^image(\s\(\d+\))?$",
    r"^video(\s\(\d+\))?$",
    r"^audio(\s\(\d+\))?$",
    r"^Screenshot.*",
    r"^copy(\s\(\d+\))?$",
    r"^temp.*",
    r"^tmp.*",
]