import time
from pyrogram import Client, filters

cooldown_tracker = {}
COOLDOWN_TIME = 60

@Client.on_message(filters.command(["ping", "help", "start", "status"]))
def anti_spam(client, message):
    user_id = message.from_user.id
    current_time = time.time()

    if user_id in cooldown_tracker:
        last_used_time = cooldown_tracker[user_id]
        time_diff = current_time - last_used_time

        if time_diff < COOLDOWN_TIME:
            remaining_time = int(COOLDOWN_TIME - time_diff)
            message.reply_text(
                f"🚫 **You're on cooldown!**\n⏳ Please wait **{remaining_time} seconds**."
            )
            return

    cooldown_tracker[user_id] = current_time
    message.reply_text("✅ Command received!")
