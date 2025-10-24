import os
import asyncio

# İstersen uvloop'u kapat: DISABLE_UVLOOP=true
if os.getenv("DISABLE_UVLOOP", "").lower() not in ("1", "true", "yes"):
    try:
        import uvloop  # type: ignore
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    except Exception:
        # Uyumlu değilse sessizce varsayılana düş
        pass