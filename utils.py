import random
import time
from datetime import datetime
from database import add_log

# ✅ Random Delay Function
def random_delay(min_delay=10, max_delay=30):
    delay = random.randint(min_delay, max_delay)
    print(f"⏳ Waiting for {delay} seconds...")
    time.sleep(delay)

# ✅ Logger Function (Log actions to the database)
def log_action(action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {action}"
    print(log_message)
    add_log(log_message)

# ✅ Time Formatter Function
def format_time(seconds):
    """Convert seconds to a human-readable format (HH:MM:SS)."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds %= 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

# ✅ Error Handler
def error_handler(function):
    """Decorator to handle errors in bot functions."""
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            log_action(f"⚠️ Error in {function.__name__}: {e}")
            print(f"❌ Error: {e}")
    return wrapper
