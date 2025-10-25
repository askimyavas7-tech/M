# ArchMusic/core/call.py

import asyncio
from pyrogram import Client
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import AudioPiped
from pytgcalls.exceptions import GroupCallNotFound
import logging

class CallManager:
    def __init__(self, client: Client):
        self.client = client
        self.call = PyTgCalls(client)
        logging.basicConfig(level=logging.INFO)

    async def start(self):
        try:
            await self.call.start()
            logging.info("✅ Ses sistemi (PyTgCalls) başlatıldı.")
        except Exception as e:
            logging.error(f"❌ Ses sistemi başlatılamadı: {e}")

    async def play(self, chat_id, audio_file):
        try:
            await self.call.join_group_call(
                chat_id,
                AudioPiped(audio_file),
            )
            logging.info(f"🎵 Ses çalınıyor: {audio_file}")
        except GroupCallNotFound:
            logging.warning("⚠️ Grup çağrısı bulunamadı, tekrar dene.")
        except Exception as e:
            logging.error(f"❌ Ses çalma hatası: {e}")

    async def stop(self):
        try:
            await self.call.stop()
            logging.info("🛑 Ses sistemi durduruldu.")
        except Exception:
            pass
