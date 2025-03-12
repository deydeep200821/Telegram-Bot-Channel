import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Telegram API Keys
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Head Owner and Roles Settings
HEAD_OWNER_ID = int(os.getenv("HEAD_OWNER_ID"))
ACTING_HEAD_OWNER_ID = int(os.getenv("ACTING_HEAD_OWNER_ID"))
MAX_OWNERS = int(os.getenv("MAX_OWNERS", 10))
MAX_USERS = int(os.getenv("MAX_USERS", 500))
MAX_GROUPS = int(os.getenv("MAX_GROUPS", 15))

# Database Settings
USE_SQLITE = os.getenv("USE_SQLITE", "True").lower() == "true"
USE_MONGODB = os.getenv("USE_MONGODB", "False").lower() == "true"
USE_POSTGRES = os.getenv("USE_POSTGRES", "False").lower() == "true"
DB_URL = os.getenv("DB_URL", "sqlite:///bot_database.db")
MONGO_URI = os.getenv("MONGO_URI", "")
POSTGRES_URL = os.getenv("POSTGRES_URL", "")

# Logging & Backup Settings
BACKUP_CHAT_ID = int(os.getenv("BACKUP_CHAT_ID"))
LOGS_CHAT_ID = int(os.getenv("LOGS_CHAT_ID"))
AUTO_BACKUP = os.getenv("AUTO_BACKUP", "True").lower() == "true"
BACKUP_INTERVAL_DAYS = int(os.getenv("BACKUP_INTERVAL_DAYS", 30))

# Security & Ban Protection Settings
FAIL2BAN_ENABLED = os.getenv("FAIL2BAN_ENABLED", "True").lower() == "true"
AUTO_RESTART = os.getenv("AUTO_RESTART", "True").lower() == "true"
WARNING_LIMIT = int(os.getenv("WARNING_LIMIT", 3))
ANTI_BAN_PROTECTION = os.getenv("ANTI_BAN_PROTECTION", "True").lower() == "true"

# Proxy Settings
PROXY_ENABLED = os.getenv("PROXY_ENABLED", "False").lower() == "true"
PROXY_URL = os.getenv("PROXY_URL", "")

# Engagement Settings
ENGAGEMENT_MIN_DELAY = int(os.getenv("ENGAGEMENT_MIN_DELAY", 10))
ENGAGEMENT_MAX_DELAY = int(os.getenv("ENGAGEMENT_MAX_DELAY", 30))

# Fail2Ban Settings
BAN_TIME = int(os.getenv("BAN_TIME", 3600))
MAX_RETRY = int(os.getenv("MAX_RETRY", 3))
