import os
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN

# Bot initialization
app = Client(
    "TelegramBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Start Command
@app.on_message(filters.command("start"))
def start_command(client, message):
    message.reply_text(f"👋 Hello {message.from_user.first_name}, I’m alive and running!")

# Help Command
@app.on_message(filters.command("help"))
def help_command(client, message):
    message.reply_text(
        "✨ **Available Commands:**\n"
        "/start - Start the bot\n"
        "/help - Get this help message\n"
        "/status - Check bot status"
    )

# Status Command
@app.on_message(filters.command("status"))
def status_command(client, message):
    message.reply_text("✅ Bot is running smoothly!")

# Bot start function
def start_bot():
    print("✅ Bot is connected!")
    app.run()
