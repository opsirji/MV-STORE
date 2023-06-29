#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5436568738:AAHPURqXFmKixCfTQBxGAzccuqaqv9-msxg")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "27100881"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ba917e1a377fa4ea750d9253bcaf9940")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001879867588"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1936430521"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://mvstore:mvstore@cluster0.00dl2o7.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "mvstore")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001713726502"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴠɪᴅᴇᴏs ᴀɴᴅ ᴅᴏᴄᴜᴍᴇɴᴛs ᴀɴᴅ ɪᴛ ᴄᴀɴ ᴀᴄᴄᴇss ʙʏ sᴘᴇᴄɪᴀʟ ʟɪɴᴋs ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ꜰʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ 📎\n\nɴᴏᴛᴇ - ᴅᴏɴ'ᴛ ꜰᴏʀᴡᴀʀᴅ ᴘᴏʀɴ ꜰɪʟᴇs ᴛᴏ ᴍᴇ, ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ 🔞\n\n📊 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ - <a href='https://t.me/hdmaxx'>ʜᴅᴍᴀxx</a></b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1936430521").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ\n\nᴋɪɴᴅʟʏ ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>📝 ꜰɪʟᴇ ɴᴀᴍᴇ:- {filename}\n\n⚖️ sɪᴢᴇ:- {filesize}</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
