from pyrogram import Client, filters

@Client.on_message(filters.command("roll"))
def roll_dice(client, message):
    message.reply_dice(emoji="🎲")
