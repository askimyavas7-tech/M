import os
def ensure_directories() -> None:
    for d in ["downloads", "cache", "logs", "cookies"]:
        os.makedirs(d, exist_ok=True)
    print("[INFO] - ArchMusic.core.dir - Directories Updated.")
