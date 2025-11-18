import os

API_ID = API_ID = 32402877 

API_HASH = os.environ.get("API_HASH", "145427eddb5c1bc4dc943d0a89f0f98b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8458145401:AAGVWdj2-kWFk6oVSDrY_0IFk1XNzN5T7Fc")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", ))

LOG = ,

# UPDATE_GRP = , # bot sat group

# auth_chats = []100179526608

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "502980590").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


