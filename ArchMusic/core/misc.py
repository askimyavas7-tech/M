import os
from typing import Set
def init_database() -> None:
    print("[INFO] - ArchMusic.misc - Database Initialized.")
def load_sudoers() -> Set[int]:
    raw = os.getenv("OWNER_ID", "") or ""
    try:
        sudos = {int(x) for x in raw.split() if x.strip()}
    except Exception:
        sudos = set()
    print("[INFO] - ArchMusic.misc - Sudoers Loaded.")
    return sudos
