from py_tgcalls import PyTgCalls
from py_tgcalls.types import AudioPiped, VideoPiped, StreamType
from pyrogram import Client

class CallManager:
    def __init__(self, app: Client):
        self.app = app
        self.tgcalls = PyTgCalls(app)

    async def start(self):
        await self.tgcalls.start()

    async def stop(self):
        await self.tgcalls.stop()

    async def join_audio(self, chat_id: int, file_path: str):
        return await self.tgcalls.join_group_call(
            chat_id, AudioPiped(file_path), stream_type=StreamType().local_stream
        )

    async def join_video(self, chat_id: int, file_path: str):
        return await self.tgcalls.join_group_call(
            chat_id, VideoPiped(file_path), stream_type=StreamType().local_stream
        )

    async def leave(self, chat_id: int):
        return await self.tgcalls.leave_group_call(chat_id)
