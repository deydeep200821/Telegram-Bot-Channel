from pyrogram import Client, filters

@Client.on_message(filters.new_chat_members)
def welcome(client, message):
    for member in message.new_chat_members:
        message.reply_text(
            f"👋 Welcome, {member.mention}!\n✨ Enjoy the group & stay active!\n\nRadhe Radhe 💞"
        )
