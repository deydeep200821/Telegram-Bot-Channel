import requests
from pyrogram import Client, filters

# ✅ Track active chat sessions
active_chats = set()

# 🔥 API setup (from .env file)
import os
API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateText"

# 🎯 /chat command se AI chat start hoga
@Client.on_message(filters.command("chat"))
def start_chat(client, message):
    user_id = message.from_user.id

    if user_id in active_chats:
        message.reply_text("⚠️ You're already in AI chat mode! Send /stop to exit.")
    else:
        active_chats.add(user_id)
        message.reply_text(
            "🤖 **Google Gemini AI Mode Activated!**\n💬 **Ask me anything — I’m listening.**\n\n🔹 Send /stop to exit."
        )


# 💬 Gemini API Integration (Optimized for speed & low RAM)
@Client.on_message(filters.text & filters.incoming)
def chat_with_gemini(client, message):
    user_id = message.from_user.id

    if user_id in active_chats:
        user_input = message.text

        # 🛠️ Gemini API Call (lightweight)
        try:
            response = requests.post(
                f"{GEMINI_API_URL}?key={API_KEY}",
                headers={"Content-Type": "application/json"},
                json={"prompt": {"text": user_input}}
            )

            # ✅ Extract AI's reply
            ai_reply = response.json().get("candidates", [{}])[0].get("output", "⚠️ I’m having trouble responding!")

            # ✨ Bot sends the AI's response back
            message.reply_text(ai_reply)

        except Exception as e:
            message.reply_text(f"⚠️ **Error:** {e}")


# 🛑 /stop command AI chat session ko band karega
@Client.on_message(filters.command("stop"))
def stop_chat(client, message):
    user_id = message.from_user.id

    if user_id in active_chats:
        active_chats.remove(user_id)
        message.reply_text("✅ **AI Chat mode exited!**\nYou're back to normal mode.")
    else:
        message.reply_text("⚠️ You're not in AI chat mode!")
