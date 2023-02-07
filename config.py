import os

class API:
    API_ID = int(os.getenv("API_ID", "27793831"))
    API_HASH = os.getenv("API_HASH", "4a101e0880f6a511f5b19e05edec3cc5")

class TOKENS:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "6088731540:AAGvrZdi78-lNRq7x5hy3KAJ88xx7G81ya4")
    STRING_SESSION = os.getenv("STRING_SESSION", "BQCeGMmfffnoAgJ6vR9LNDSPbrY30rHrJgsi_778Jk5wUOOJKNwemJLOiJWrkq_G99v6kUioxOB5eidb9vyc6Km-pfU0MQhwF3XyY1rfU_01WhA-mupOoUZYaqdB0QtEz0cMiT9pLrOdN7xp5pWNBWYUI5Nqk3pnkZSSG7YEPujoQr8JQIJqEPlbR-2bk5u4sAGKN7JoLlyZ_GHyhmtbWKup4w49MZ3WuLzMcUMyc7L4guNj3JTh2iWyndIvnaZKLbsW_m_WvVaG2tGWI0cB4NLwPShWUHaajAXLlir7z3_Mrek0NqUjZ1BmabL4ZPERVX9zIzm-cfsZN0g4LSliFZG5AAAAAVEVII0A")
    STRING_SESSION_2 = os.getenv("STRING_SESSION_2", "")
    STRING_SESSION_3 = os.getenv("STRING_SESSION_3", "")
    STRING_SESSION_4 = os.getenv("STRING_SESSION_4", "")
    STRING_SESSION_5 = os.getenv("STRING_SESSION_5", "")
    STRING_SESSION_6 = os.getenv("STRING_SESSION_6", "")
    STRING_SESSION_7 = os.getenv("STRING_SESSION_7", "")
    STRING_SESSION_8 = os.getenv("STRING_SESSION_8", "")
    STRING_SESSION_9 = os.getenv("STRING_SESSION_9", "")
    STRING_SESSION_10 = os.getenv("STRING_SESSION_10", "")

class DATABASE:
    MONGO_DB_URL = os.getenv("MONGO_DB_URL", "mongodb+srv://Hi_shivaay:<password>@cluster0.mdctz5d.mongodb.net/?retryWrites=true&w=majority")

class DEV:
    OWNER_ID = int(os.getenv("OWNER_ID", "5655306381"))
    
    # DONT EDIT THIS 
    SUDO_USERS = [5767907357] 
    # YOU CAN ADD SUDO USING /addsudo

class STUFF:
    ALIVE_PIC = os.getenv("ALIVE_PIC", "https://telegra.ph/file/ee95320ee5f2f7a3e3ef9.jpg")
    HELP_PIC = os. getenv("HELP_PIC", "https://telegra.ph/file/beead917f9c42d471380d.jpg")
    START_PIC = os. getenv("START_PIC", "https://telegra.ph/file/26be3ad04aa29730ce162.jpg")
    COMMAND_HANDLER = os. getenv("COMMAND_HANDLER", "!")
