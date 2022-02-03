import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "santhu_music_bot")
ALIVE_NAME = getenv("ALIVE_NAME", "⭐sᴀɴᴛʜᴏsʜ ⭕")
BOT_USERNAME = getenv("BOT_USERNAME", "luckyvideobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "cute_boy701")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "terayaarhoomai")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "maxopeditz")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5023234844").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/b921645cc124c9d7acf7c.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/mrvk1703/video-stream")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/ffbb096d10dd36ad45337.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/e719f19bbeeb7f55e6202.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/9462e6eba7e79c3f65779.jpg")
