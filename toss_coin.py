import random
from pyrogram import Client, filters

# 🔥 Toss Command Setup
@Client.on_message(filters.command("toss"))
def coin_toss(client, message):
    # 🪙 Bot toss karega — Heads or Tails
    result = random.choice(["Heads", "Tails"])

    # 🔥 Bot se user ko choice lene ka prompt
    message.reply_text("🪙 Tossing the coin...🤔\n**Heads or Tails?**")

    # 🔥 2-second delay for suspense
    client.send_message(
        message.chat.id,
        "🕒 *Tossing...*",
        disable_notification=True,
    )

    # ✨ Bot ka toss result
    client.send_message(
        message.chat.id,
        f"✅ **Result:** 🎉 **{result}!**"
    )
