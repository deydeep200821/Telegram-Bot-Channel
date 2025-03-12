#!/bin/bash

echo "🔍 Monitoring bot status..."

# Infinite loop to keep bot running
while true; do
    # Start the bot
    python3 main.py
    
    # If the bot crashes, log the time and restart
    echo "⚠️ Bot crashed! Restarting..." >> bot_crash.log
    date >> bot_crash.log

    # Wait for 5 seconds before restarting
    sleep 5
done
