import os
import asyncio
from pyrogram import Client, idle
from ArchMusic.core.logger import setup_logging
from ArchMusic.core.dir import ensure_directories
from ArchMusic.core.misc import init_database, load_sudoers
from ArchMusic.core.git import fetch_updates
from ArchMusic.core.call import CallManager

# ✅ Heroku - asyncio hatasını çözer
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

class ArchMusicBot:
    def __init__(self):
        self.log = setup_logging("INFO")
        ensure_directories()
        init_database()
        load_sudoers()

        api_id = int(os.getenv("API_ID", "0"))
        api_hash = os.getenv("API_HASH", "")
        bot_token = os.getenv("BOT_TOKEN", "")

        if not api_id or not api_hash or not bot_token:
            raise RuntimeError(
                "⚠️ API_ID / API_HASH / BOT_TOKEN eksik!\n"
                "➡️ Heroku Config Vars bölümüne eklemeyi unutma."
            )

        self.app = Client(
            "ArchMusic",
            api_id=api_id,
            api_hash=api_hash,
            bot_token=bot_token,
            workers=8,
            in_memory=True,
        )

        self.call = CallManager(self.app)

        upstream = os.getenv("UPSTREAM_REPO")
        if upstream:
            fetch_updates(upstream)

    async def _amain(self):
        self.log.info("✅ ArchMusic başlatılıyor...")
        await self.app.start()
        await self.call.start()
        self.log.info("🎵 Bot aktif! Kullanıcı mesajlarını bekliyor...")
        await idle()
        await self.call.stop()
        await self.app.stop()

    def run(self):
        try:
            asyncio.run(self._amain())
        except RuntimeError:
            # ✅ asyncio.run hatası olursa alternatif başlatma
            loop = asyncio.new_event_loop()
            loop.run_until_complete(self._amain())
        except KeyboardInterrupt:
            self.log.warning("🛑 Bot manuel olarak durduruldu.")
