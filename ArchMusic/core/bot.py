# ArchMusic/core/bot.py
import os
import asyncio

# ✅ Pyrogram importundan ÖNCE event loop'u garanti et
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from pyrogram import Client, idle
from ArchMusic.core.logger import setup_logging
from ArchMusic.core.dir import ensure_directories  # repoda bu fonksiyon var
from ArchMusic.core.misc import init_database, load_sudoers
from ArchMusic.core.git import fetch_updates
from ArchMusic.core.call import CallManager


class ArchMusicBot:
    def __init__(self):
        self.log = setup_logging("INFO")

        # Temel hazırlıklar
        try:
            ensure_directories()
        except Exception:
            # Bazı repolarda ensure_directories adı farklı olabilir;
            # sessiz geç, kritik değil
            pass

        try:
            init_database()
        except Exception:
            pass

        try:
            load_sudoers()
        except Exception:
            pass

        api_id = int(os.getenv("API_ID", "0"))
        api_hash = os.getenv("API_HASH", "")
        bot_token = os.getenv("BOT_TOKEN", "")

        if not api_id or not api_hash or not bot_token:
            raise RuntimeError(
                "API_ID / API_HASH / BOT_TOKEN eksik. Heroku Settings → Config Vars kısmını kontrol et."
            )

        self.app = Client(
            name="ArchMusic",
            api_id=api_id,
            api_hash=api_hash,
            bot_token=bot_token,
            in_memory=True,
            workers=8,
        )
        self.call = CallManager(self.app)

        upstream = os.getenv("UPSTREAM_REPO")
        if upstream:
            try:
                fetch_updates(upstream)
            except Exception:
                # Upstream opsiyonel—hata verirse botu durdurmasın
                pass

    async def _amain(self):
        self.log.info("✅ ArchMusic: bot başlatılıyor...")
        await self.app.start()
        await self.call.start()
        self.log.info("🎵 Bot aktif. Komutları bekliyor...")
        await idle()
        self.log.info("🛑 Durduruluyor...")
        await self.call.stop()
        await self.app.stop()

    def run(self):
        try:
            asyncio.run(self._amain())
        except RuntimeError:
            # Bazı ortamlarda asyncio.run hata verirse alternatif akış
            loop = asyncio.new_event_loop()
            loop.run_until_complete(self._amain())
        except KeyboardInterrupt:
            self.log.warning("🟡 Manuel olarak durduruldu.")
