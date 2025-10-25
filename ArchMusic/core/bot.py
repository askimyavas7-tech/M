# ArchMusic/core/bot.py

import os
import asyncio

# ✅ Pyrogram başlamadan önce event loop oluştur
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from pyrogram import Client, idle
from ArchMusic.core.logger import setup_logging
from ArchMusic.core.misc import init_database, load_sudoers
from ArchMusic.core.git import fetch_updates
from ArchMusic.core.call import CallManager


class ArchMusicBot:
    def __init__(self):
        self.log = setup_logging("INFO")

        # ✅ ENV ÇEK
        api_id = int(os.getenv("API_ID", "0"))
        api_hash = os.getenv("API_HASH", "")
        bot_token = os.getenv("BOT_TOKEN", "")

        if not api_id or not api_hash or not bot_token:
            raise RuntimeError(
                "API_ID / API_HASH / BOT_TOKEN eksik.\n➡ Heroku Config Vars kısmından ekle!"
            )

        # ✅ PYROGRAM BOT
        self.app = Client(
            "ArchMusic",
            api_id=api_id,
            api_hash=api_hash,
            bot_token=bot_token,
            plugins=dict(root="ArchMusic.plugins")  # <-- PLUGINS AKTİF ❗
        )

        # ✅ SES SİSTEMİ
        self.call = CallManager(self.app)

        # ✅ DATABASE & SUDO
        try:
            init_database()
            load_sudoers()
        except:
            pass

        # ✅ Upstream Repo Güncellemesi (opsiyonel)
        upstream = os.getenv("UPSTREAM_REPO")
        if upstream:
            try:
                fetch_updates(upstream)
            except:
                pass

    async def start_bot(self):
        self.log.info("✅ ArchMusic başlatılıyor...")
        await self.app.start()
        await self.call.start()
        self.log.info("🎧 Bot aktif. Komutlar bekleniyor.")
        await idle()
        await self.stop_bot()

    async def stop_bot(self):
        self.log.info("🛑 Bot durduruluyor...")
        await self.call.stop()
        await self.app.stop()

    def run(self):
        try:
            asyncio.run(self.start_bot())
        except RuntimeError:
            loop = asyncio.new_event_loop()
            loop.run_until_complete(self.start_bot())
        except KeyboardInterrupt:
            self.log.warning("⚠ Bot manuel olarak durduruldu.")


# ✅ ÇALIŞTIRICI
if __name__ == "__main__":
    bot = ArchMusicBot()
    bot.run()
