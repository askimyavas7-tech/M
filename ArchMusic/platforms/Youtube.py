import asyncio
import os
import re
from typing import Union
from yt_dlp import YoutubeDL
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from youtubesearchpython.__future__ import VideosSearch
from ArchMusic.utils.database import is_on_off
from ArchMusic.utils.formatters import time_to_seconds

def cookiefile() -> str:
    cookie_dir = "cookies"
    if not os.path.isdir(cookie_dir):
        raise FileNotFoundError("cookies/ directory not found")
    cookies_files = [f for f in os.listdir(cookie_dir) if f.endswith(".txt")]
    if not cookies_files:
        raise FileNotFoundError("No .txt cookie file found in cookies/")
    return os.path.join(cookie_dir, cookies_files[0])

async def shell_cmd(cmd: str) -> str:
    proc = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    out, err = await proc.communicate()
    if err and "unavailable videos are hidden" not in (err.decode("utf-8")).lower():
        return err.decode("utf-8")
    return out.decode("utf-8")

class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.regex = r"(?:youtube\.com|youtu\.be)"
        self.listbase = "https://youtube.com/playlist?list="

    async def url(self, message_1: Message) -> Union[str, None]:
        messages = [message_1]
        if message_1.reply_to_message:
            messages.append(message_1.reply_to_message)
        for message in messages:
            if message.entities:
                for entity in message.entities:
                    if entity.type == MessageEntityType.URL:
                        text = message.text or message.caption
                        return text[entity.offset: entity.offset + entity.length]
            if message.caption_entities:
                for entity in message.caption_entities:
                    if entity.type == MessageEntityType.TEXT_LINK:
                        return entity.url
        return None

    async def exists(self, link: str, videoid: Union[bool, str] = None) -> bool:
        if videoid:
            link = self.base + link
        return bool(re.search(self.regex, link))

    async def details(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        link = link.split("&")[0] if "&" in link else link
        search = VideosSearch(link, limit=1)
        data = (await search.next()).get("result", [])
        if not data:
            return None
        item = data[0]
        title = item.get("title")
        duration_min = item.get("duration")
        thumbnail = (item.get("thumbnails", [{}])[0].get("url", "")).split("?")[0]
        vidid = item.get("id")
        duration_sec = int(time_to_seconds(duration_min)) if duration_min else 0
        return title, duration_min, duration_sec, thumbnail, vidid

    async def track(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        link = link.split("&")[0] if "&" in link else link
        search = VideosSearch(link, limit=1)
        data = (await search.next()).get("result", [])
        if not data:
            return None, None
        item = data[0]
        title = item.get("title")
        duration_min = item.get("duration")
        vidid = item.get("id")
        yturl = item.get("link")
        thumbnail = (item.get("thumbnails", [{}])[0].get("url", "")).split("?")[0]
        track_details = {
            "title": title,
            "link": yturl,
            "vidid": vidid,
            "duration_min": duration_min,
            "thumb": thumbnail,
            "cookiefile": cookiefile(),
        }
        return track_details, vidid

    async def slider(self, link: str, query_type: int, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        link = link.split("&")[0] if "&" in link else link
        search = VideosSearch(link, limit=10)
        data = (await search.next()).get("result", [])
        if not data or query_type >= len(data):
            return None, None, None, None
        item = data[query_type]
        title = item.get("title")
        duration_min = item.get("duration")
        vidid = item.get("id")
        thumbnail = (item.get("thumbnails", [{}])[0].get("url", "")).split("?")[0]
        return title, duration_min, thumbnail, vidid

    async def formats(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        link = link.split("&")[0] if "&" in link else link
        ydl_opts = {"quiet": True, "cookiefile": cookiefile()}
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=False)
            formats_available = []
            for f in info.get("formats", []):
                try:
                    if "dash" in str(f.get("format", "")).lower():
                        continue
                    formats_available.append(
                        {
                            "format": f.get("format"),
                            "filesize": f.get("filesize"),
                            "format_id": f.get("format_id"),
                            "ext": f.get("ext"),
                            "format_note": f.get("format_note"),
                            "yturl": link,
                            "cookiefile": cookiefile(),
                        }
                    )
                except Exception:
                    continue
        return formats_available, link

    async def download(
        self,
        link: str,
        mystic=None,
        video: Union[bool, str] = None,
        videoid: Union[bool, str] = None,
        songaudio: Union[bool, str] = None,
        songvideo: Union[bool, str] = None,
        format_id: Union[bool, str] = None,
        title: Union[bool, str] = None,
    ):
        if videoid:
            link = self.base + link

        loop = asyncio.get_running_loop()

        def audio_dl():
            opts = {
                "cookiefile": cookiefile(),
                "format": "bestaudio/best",
                "outtmpl": "downloads/%(id)s.%(ext)s",
                "geo_bypass": True,
                "nocheckcertificate": True,
                "quiet": True,
                "no_warnings": True,
            }
            with YoutubeDL(opts) as ydl:
                info = ydl.extract_info(link, False)
                path = os.path.join("downloads", f"{info['id']}.{info['ext']}")
                if not os.path.exists(path):
                    ydl.download([link])
                return path

        def video_dl():
            opts = {
                "cookiefile": cookiefile(),
                "format": "(best[height<=?720][width<=?1280])",
                "outtmpl": "downloads/%(id)s.%(ext)s",
                "geo_bypass": True,
                "nocheckcertificate": True,
                "quiet": True,
                "no_warnings": True,
            }
            with YoutubeDL(opts) as ydl:
                info = ydl.extract_info(link, False)
                path = os.path.join("downloads", f"{info['id']}.{info['ext']}")
                if not os.path.exists(path):
                    ydl.download([link])
                return path

        def song_video_dl():
            fpath = f"downloads/{title}"
            opts = {
                "cookiefile": cookiefile(),
                "format": f"{format_id}+140",
                "outtmpl": fpath,
                "geo_bypass": True,
                "nocheckcertificate": True,
                "quiet": True,
                "no_warnings": True,
                "prefer_ffmpeg": True,
                "merge_output_format": "mp4",
            }
            with YoutubeDL(opts) as ydl:
                ydl.download([link])

        def song_audio_dl():
            fpath = f"downloads/{title}.%(ext)s"
            opts = {
                "cookiefile": cookiefile(),
                "format": format_id,
                "outtmpl": fpath,
                "geo_bypass": True,
                "nocheckcertificate": True,
                "quiet": True,
                "no_warnings": True,
                "prefer_ffmpeg": True,
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ],
            }
            with YoutubeDL(opts) as ydl:
                ydl.download([link])

        if songvideo:
            await loop.run_in_executor(None, song_video_dl)
            return f"downloads/{title}.mp4"
        elif songaudio:
            await loop.run_in_executor(None, song_audio_dl)
            return f"downloads/{title}.mp3"
        elif video:
            if await is_on_off(1):
                return await loop.run_in_executor(None, video_dl)
        return await loop.run_in_executor(None, audio_dl)
