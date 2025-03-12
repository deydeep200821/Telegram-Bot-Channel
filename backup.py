import os
import shutil
from datetime import datetime
from pyrogram import Client
from config import BACKUP_CHAT_ID, HEAD_OWNER_ID, BOT_TOKEN, API_ID, API_HASH

# Bot client setup for sending backups
app = Client(
    "backup_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ✅ Backup function
def create_backup():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_folder = f"backup_{timestamp}"

    # Create backup folder
    os.makedirs(backup_folder, exist_ok=True)

    # Copy database
    if os.path.exists("bot_database.db"):
        shutil.copy("bot_database.db", f"{backup_folder}/bot_database.db")

    # Copy logs
    if os.path.exists("bot_crash.log"):
        shutil.copy("bot_crash.log", f"{backup_folder}/bot_crash.log")

    # Copy config file
    shutil.copy("config.py", f"{backup_folder}/config_backup.py")

    # Zip the backup folder
    backup_zip = f"{backup_folder}.zip"
    shutil.make_archive(backup_folder, 'zip', backup_folder)
    shutil.rmtree(backup_folder)

    return backup_zip

# ✅ Send backup file to Telegram (Head Owner + Private Channel)
def send_backup():
    backup_file = create_backup()
    with app:
        # Send to private backup channel
        app.send_document(BACKUP_CHAT_ID, backup_file, caption="📦 **New Backup Created!**")
        
        # Send to Head Owner directly
        app.send_document(HEAD_OWNER_ID, backup_file, caption="✅ **Your Bot's Latest Backup!**")
    
    # Delete local backup file after sending
    os.remove(backup_file)
    print("✅ Backup completed and sent!")

# ✅ If run directly, create and send backup
if __name__ == "__main__":
    print("🔄 Creating backup...")
    send_backup()
