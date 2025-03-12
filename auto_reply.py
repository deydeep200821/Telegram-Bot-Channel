from pyrogram import Client, filters

@Client.on_message(filters.text & ~filters.private)
def auto_reply(client, message):
    if "hello" in message.text.lower():
        message.reply_text("👋 Hello! Radhe Radhe 💞")
    elif "bye" in message.text.lower():
        message.reply_text("👋 Bye! Take care 💞")
