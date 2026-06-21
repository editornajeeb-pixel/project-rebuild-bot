import os
from pathlib import Path
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent
load_dotenv(ROOT_DIR / ".env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")

if not BOT_TOKEN:
    raise RuntimeError(
        "Missing BOT_TOKEN. Set BOT_TOKEN in .env or Railway environment variables."
    )

if not SPREADSHEET_ID:
    raise RuntimeError(
        "Missing SPREADSHEET_ID. Set SPREADSHEET_ID in .env or Railway environment variables."
    )
 