from pathlib import Path


BASE_DIR = Path(__file__).resolve(strict=True).parent

DB_NAME = BASE_DIR / 'db.sqlite3'
