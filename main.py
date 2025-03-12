import os
import importlib
from bot import start_bot

# Feature loader setup
def load_features():
    features_folder = "features"
    if os.path.exists(features_folder):
        for filename in os.listdir(features_folder):
            if filename.endswith(".py"):
                feature_name = filename[:-3]
                try:
                    importlib.import_module(f"features.{feature_name}")
                    print(f"✅ Loaded feature: {feature_name}")
                except Exception as e:
                    print(f"⚠️ Error loading feature {feature_name}: {e}")

# Bot start with feature loading
if __name__ == "__main__":
    print("🚀 Starting Telegram Bot...")
    load_features()  # Load all features from "features" folder
    start_bot()
