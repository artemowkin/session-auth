import sqlite3

from settings import DB_NAME


connection = sqlite3.connect(DB_NAME)

__all__ = ['connection']
