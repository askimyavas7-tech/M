import subprocess
def fetch_updates(repo_url: str) -> None:
    try:
        subprocess.run(["git", "fetch", "--all"], check=False)
        subprocess.run(["git", "pull", "--no-edit", repo_url], check=False)
        print(f"[INFO] - ArchMusic.core.git - Fetched Updates from: {repo_url}")
    except Exception as e:
        print("[WARN] - ArchMusic.core.git - Git fetch skipped:", e)
