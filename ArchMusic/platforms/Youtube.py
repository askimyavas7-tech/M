# Copyright (C) 2025 by Alexa_Help @ Github
# Clean final version — No cookies, with YouTube API key and url() method.

import asyncio
import os
import re
from typing import Union

from yt_dlp import YoutubeDL
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from youtubesearchpython.__future__ import VideosSearch

import config
from ArchMusic.utils.database import is_on_off
from ArchMusic.utils.formatters import time_to_seconds


async def shell_cmd(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    out, errorz = await proc.communicate()
    if errorz:
        if "unavailable videos are hidden" in (errorz.decode("utf-8")).lower():
            return out.decode("utf-8")
        else:
            return errorz.decode("utf-8")
    return out.decode("utf-8")


class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.regex = r"(?:youtube\\.com|youtu\\.be)"
        self.status = "https://www.youtube.com/oembed?url="
        self.listbase = "https://youtube.com/playlist?list="
        self.reg = re.compile(r"\\x1B(?:[@-Z\\\\-_]|\\[[0-?]*[ -/]*[@-~])")

    # 🔹 Yeni eklendi: url() metodu
    async def url(self, message_1: Message) -> Union[str, None]:
        messages = [message_1]
        if message_1.reply_to_message:
            messages.append(message_1.reply_to_message)
        text = ""
        offset = None
        length = None
        for message in messages:
            if offset:
                break
            if message.entities:
                for entity in message.entities:
                    if entity.type == MessageEntityType.URL:
                        text = message.text or message.caption
                        offset, length = entity.offset, entity.length
                        break
            elif message.caption_entities:
                for entity in message.caption_entities:
                    if entity.type == MessageEntityType.TEXT_LINK:
                        return entity.url
        if offset in (None,):
            return None
        return text[offset : offset + length]

    async def exists(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        return bool(re.search(self.regex, link))

    async def details(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1, api_key=config.YOUTUBE_API_KEY)
        for result in (await results.next())["result"]:
            title = result["title"]
            duration_min = result["duration"]
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            vidid = result["id"]
            duration_sec = int(time_to_seconds(duration_min)) if duration_min else 0
        return title, duration_min, duration_sec, thumbnail, vidid

    async def track(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1, api_key=config.YOUTUBE_API_KEY)
        for result in (await results.next())["result"]:
            title = result["title"]
            duration_min = result["duration"]
            vidid = result["id"]
            yturl = result["link"]
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        return {
            "title": title,
            "link": yturl,
            "vidid": vidid,
            "duration_min": duration_min,
            "thumb": thumbnail,
        }, vidid

    async def slider(self, link: str, query_type: int, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        a = VideosSearch(link, limit=10, api_key=config.YOUTUBE_API_KEY)
        result = (await a.next()).get("result")
        title = result[query_type]["title"]
        duration_min = result[query_type]["duration"]
        vidid = result[query_type]["id"]
        thumbnail = result[query_type]["thumbnails"][0]["url"].split("?")[0]
        return title, duration_min, thumbnail, vidid

    async def download(
        self,
        link: str,
        video: Union[bool, str] = None,
        songaudio: Union[bool, str] = None,
        songvideo: Union[bool, str] = None,
        format_id: Union[bool, str] = None,
        title: Union[bool, str] = None,
    ):
        loop = asyncio.get_running_loop()

        def audio_dl():
            opts = {
                "format": "bestaudio/best",
                "outtmpl": "downloads/%(id)s.%(ext)s",
                "geo_bypass": True,
                "youtube_api_key": config.YOUTUBE_API_KEY,
                "quiet": True,
                "no_warnings": True,
            }
            ydl = YoutubeDL(opts)
            info = ydl.extract_info(link, False)
            file_path = os.path.join("downloads", f"{info['id']}.{info['ext']}")
            if not os.path.exists(file_path):
                ydl.download([link])
            return file_path

        def video_dl():
            opts = {
                "format": "(best[height<=?720][width<=?1280])",
                "outtmpl": "downloads/%(id)s.%(ext)s",
                "geo_bypass": True,
                "youtube_api_key": config.YOUTUBE_API_KEY,
                "quiet": True,
                "no_warnings": True,
            }
            ydl = YoutubeDL(opts)
            info = ydl.extract_info(link, False)
            file_path = os.path.join("downloads", f"{info['id']}.{info['ext']}")
            if not os.path.exists(file_path):
                ydl.download([link])
            return file_path

        if songvideo:
            return await loop.run_in_executor(None, video_dl)
        elif songaudio:
            return await loop.run_in_executor(None, audio_dl)
        elif video:
            if await is_on_off(1):
                return await loop.run_in_executor(None, video_dl)
        else:
            return await loop.run_in_executor(None, audio_dl)