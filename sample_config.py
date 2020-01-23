import os

class Config(object):
    
    CHAT_BASE_TOKEN = os.environ.get("9cf64d2e-9c70-439e-a66e-8cbb0b524d79", "")
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("1021135967:AAFTJxgGDBPbGbye58j-0UfGSsRbLYKxcbo", "")
    # The Telegram API things
    APP_ID = int(os.environ.get("1104007", 12345))
    API_HASH = os.environ.get("4ed43d52342463ad74846b57a28bdc4e")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("749293934", "").split())
    #For Ban
    BANNED_USERS = []
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 1572864000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("http://117.240.238.230/", "")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = "4ed43d52342463ad74846b57a28bdc4e"
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = ""
