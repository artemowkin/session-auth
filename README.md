# session-auth

This project is just for learning

In this project I tried to do session authentication using DB

## Get started

To run this project you need to install dependencies:

```
$ pipenv install
```

After that you need to initialize database:

```
$ ./main.py init
```

And run server:

```
$ gunicorn server
```

And now you can go to the http://127.0.0.1:8000.

## About

First you'll see the
message that you're an anonymous user. In the same time you received
cookie with session id and in DB was created new user. If you update
the page you'll see the message with information about user with
random 10 letters in `name` field and with some number in `user_id`

`sessionid` cookie is random 32-length string with ascii letters and digits

Your sessionid is taken from cookie and using to find session in
`sessions` table. Session has two attributes:

1. `session_id` - 32-length string with ascii letters and digits. Primary key
2. `user_id` - integer foreign key to `users` table

When we got the session entry we can identify user using `user_id` field

## Used stack

* Language: `python3.8`
* Database: `sqlite3`
* Server: `gunicorn`
