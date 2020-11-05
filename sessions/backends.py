"""Module with authentication logic

Functions
---------
generate_session_id()
    This function is using for generating session ids
init_database()
    This function is using for initialize database tables
get_user_by_id()
    This function is using for getting user by its id
get_user_by_session_id()
    This function is using for getting user by id of session related with it
create_user()
    This function is using for creating new user and session for it

"""
import string
import random
from sqlite3 import OperationalError
from typing import Iterable

from db import connection

from .users import User


def generate_session_id(size=32, chars=string.ascii_letters+string.digits):
    """
    Generate session id - 32 length string
    with ascii letters and digits
    """
    return ''.join(random.choices(chars, k=size))


def init_database() -> None:
    """Generate initial database tables

    Notes
    -----
    Table `users` has one-to-many relationships with `sessions`
    (one user can relate with many sessions, but one session can
    relate with only one user)

    """
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE users ("
        "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
        "name VARCHAR(50) NOT NULL UNIQUE"
        ");"
    )
    cursor.execute(
        "CREATE TABLE sessions("
        "session_id CHAR(32) NOT NULL PRIMARY KEY,"
        "user_id INTEGER NOT NULL,"
        "FOREIGN KEY (user_id) REFERENCES users (id)"
        ");"
    )
    cursor.close()
    connection.commit()


def get_user_by_id(user_id: int) -> User:
    """Return User object using its `id` field"""
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user_data = cursor.fetchone()
    return User(user_data)


def get_user_by_session_id(sessionid: str) -> User:
    """Return User object using session_id"""
    cursor = connection.cursor()
    # Get user related with session with sessionid
    cursor.execute(
        'SELECT * FROM users WHERE id = '
        '(SELECT user_id FROM sessions WHERE session_id = ?);',
        (sessionid,)
    )
    user_data = cursor.fetchone()
    cursor.close()
    return User(user_data)


def create_user(params: Iterable) -> tuple:
    """Create new user entry and session entry related with it

    Returns
    -------
    Tuple with user id and if of session related with it

    """
    cursor = connection.cursor()
    cursor.execute('INSERT INTO users (name) VALUES (?)', params)
    cursor.execute('SELECT id FROM users WHERE name = ?', params)
    user_id = cursor.fetchone()[0]
    session_id = generate_session_id()
    cursor.execute(
        'INSERT INTO sessions VALUES (?, ?)', (session_id, user_id)
    )
    cursor.close()
    connection.commit()
    return (user_id, session_id)
