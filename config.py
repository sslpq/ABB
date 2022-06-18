## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAA860Ij4D_MG7ojFDH1Kha-On07P1WTJUBY4pWruNS2xz9JettH9k6KvHSm-bkzkCUAWNbKU-uOZPlyIZavyTex7WshzLYT8wTaVTkUV24V-Alf-wVpPYv2PUnurWzjpnHrMZemKG3dV8zuOtV7z3tjAXl__0LeDPsf5ihLs-utPN-30A7HjcwKhNaj_JhDB7hQY7JZSjBTEKRbMf0FBF-BFyGZBU1KQuq21DF93NmpxWkcC6krb81u5jZh_r04VKc23YR6z0-NIUltDk_hj26b6E4ahKdQZROkSTJAF2Kfe_DLo7vnfURfnB5gLOia07CHFpwsqmuH4NM5b_MqpDETAAAAAUY9at0A")
BOT_TOKEN = getenv("BOT_TOKEN", "5416662309:AAGSlbL4vR_EtlTCKKbL40FfUWyCr_QrqAE")
BOT_NAME = getenv("BOT_NAME", "song")
API_ID = int(getenv("API_ID", "19207775"))
API_HASH = getenv("API_HASH", "cea2171dee6589add2c19ec28778f3d2")
OWNER_NAME = getenv("OWNER_NAME", "وكح؟")
OWNER_USERNAME = getenv("OWNER_USERNAME", "AAAQQQ")
ALIVE_NAME = getenv("ALIVE_NAME", "وكح؟")
BOT_USERNAME = getenv("BOT_USERNAME", "iooxxibot")
OWNER_ID = getenv("OWNER_ID", "5338950085")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "iooxxi")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "H_B_4")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "H_B_4")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5338950085").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/b2c045447c0cce9328618.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/89ae9824c9e373ba65361.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/b2c045447c0cce9328618.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/87b242414fece2e26536e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/b2c045447c0cce9328618.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/87b242414fece2e26536e.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/b2c045447c0cce9328618.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/87b242414fece2e26536e.jpg")
