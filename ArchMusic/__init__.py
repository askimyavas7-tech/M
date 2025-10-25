#
# ArchMusic package initializer
# Import gerekli kullanıcı ve platform API’leri
#

from ArchMusic.core.dir import dirr
from ArchMusic.core.git import git
from ArchMusic.misc import dbb, heroku, sudo
from .logging import LOGGER

# Run essential setup tasks
dirr()
git()
dbb()
heroku()
sudo()

# ✅ Bot veya Userbot burada başlatılmayacak!!
# Bunları bot.py çalıştıracak.
#
# ❌ AŞAĞIDAKİLER KALDIRILDI:
# app = ArchMusic()
# userbot = Userbot()

# ✅ Platform API’leri import edilebilir
from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

LOGGER.info("✅ ArchMusic paket yüklemesi tamamlandı.")
