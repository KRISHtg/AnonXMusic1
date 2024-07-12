import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

EVAL = list(map(int, getenv("EVAL", " ").split()))
# ------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","Its_krish_tg")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "Queen_of_heart_music_bot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "queen music")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "queen")
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", -1001864483206))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 6745609407))
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/KRISHtg/queenmusicbot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Queen_update")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Queen_update")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "500"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# Bot introduction messages - These can be customized as per your preference
AYU = [
    "💞", "🦋", "🔍", "🧪", "🦋", "⚡️", "🔥", "🦋", "", "🍷", "🥂", "🦋", "🥃", "🥤", "🕊️",
    "🦜", "🐝", "🕊️", "🧪", "🕊️", "🔎", "🦋", "🎶", "🪄", "🌡️", "🦜", "🧨"
]

AYUV = [
    "❖ нᴇʏ</b> {0}, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ !</b>\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n<b>● ʜᴇʏ, ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ꜱᴜᴘᴇʀꜰᴀꜱᴛ ᴍᴜꜱɪᴄ ʙᴏᴛ</b>\n\n<b>● ꜰᴇᴇʟ ꜰʀᴇᴇ ᴛᴏ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ, ᴀɴᴅ ᴇɴᴊᴏʏ... ɴᴏ ʟᴀɢ ᴀᴜᴅɪᴏ ᴀɴᴅ ᴠɪᴅᴇᴏ\n<b>● ᴢᴇʀᴏ ᴅᴏᴡɴᴛɪᴍᴇ ᴀɴᴅ ʟᴀɢ ꜰʀᴇᴇ ᴍᴜꜱɪᴄ 🎶\n\n<b>❖ ᴛʜɪs ɪs ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ʙᴏᴛ, ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴠᴄ.</b>\n\nʙᴏᴛ ʀᴇᴘᴏ  ➥ /repo)"
]
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/f6b2e18ecae7ffb6a9c88.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
STATS_IMG_URL = "https://telegra.ph/file/7adee139f0639c400e1b8.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/9e14789c344a3c983aca5.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/9e14789c344a3c983aca5.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/9e14789c344a3c983aca5.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
