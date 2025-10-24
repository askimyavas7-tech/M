import os, asyncio
from pyrogram import Client, idle
from ArchMusic.core.logger import setup_logging
from ArchMusic.core.dir import ensure_directories
from ArchMusic.core.misc import init_database, load_sudoers
from ArchMusic.core.git import fetch_updates
from ArchMusic.core.call import CallManager

class ArchMusicBot:
    def __init__(self):
        self.log = setup_logging("INFO")
        ensure_directories()
        init_database()
        load_sudoers()

        api_id = int(os.getenv("API_ID", "0"))
        api_hash = os.getenv("API_HASH", "")
        bot_token = os.getenv("BOT_TOKEN", "")

        if not (api_id and api_hash and bot_token):
            raise RuntimeError("API_ID / API_HASH / BOT_TOKEN is missing")

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
            fetch_updates(upstream)

    async def _amain(self):
        self.log.info("ArchMusic.core.bot - Bot Başlatılıyor")
        await self.app.start()
        await self.call.start()
        await idle()
        await self.call.stop()
        await self.app.stop()

    def run(self):
        asyncio.get_event_loop().run_until_complete(self._amain())
