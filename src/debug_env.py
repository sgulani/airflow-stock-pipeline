# src/debug_env.py

import os
from dotenv import load_dotenv

load_dotenv()

required_vars = [
    "API_KEY",
    "SYMBOL",
    "INTERVAL",
    "AWS_ACCESS_KEY_ID",
    "AWS_SECRET_ACCESS_KEY",
    "AWS_DEFAULT_REGION",
    "AWS_BUCKET_NAME"
]
print("✅ Datei läuft")

print("🔍 Überprüfe Umgebungsvariablen aus .env:\n")
for var in required_vars:
    value = os.getenv(var)
    if value is None or value.strip() == "":
        print(f"❌ {var} ist NICHT gesetzt oder leer!")
    else:
        print(f"✅ {var} = {value[:4]}...{'(verkürzt)' if len(value) > 8 else ''}")
