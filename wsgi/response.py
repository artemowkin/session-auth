import string
import random

from sessions.users import AnonymousUser
from sessions import backends


class WSGIResponse:

    """Simple response object

    Attributes
    ----------
    status : str
        Status of response
    headers : list
        Response headers
    body : bytes
        Response body

    """

    def __init__(self, status, headers, body) -> None:
        self.status = status
        self.headers = headers
        self._body = body

    @property
    def body(self):
        if isinstance(self._body, bytes):
            return self._body

        return self._body.encode()


def handle_request(request) -> WSGIResponse:
    """
    Simple request handler just for example. If user isn't authenticated
    creates a new user with random name, set cookie with session id,
    and returns info about anonymous user. If user is authenticated returns
    information about it
    """
    if isinstance(request.user, AnonymousUser):
        user_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        user_id, session_id = backends.create_user((user_name,))
        headers = [
            ('Set-Cookie',
             f'sessionid={session_id}; Max-Age=5000; HttpOnly; Path=/'),
            ('Content-Type', 'text/plain'),
        ]
    else:
        headers = [('Content-Type', 'text/plain')]

    status = '200 OK'
    body = (
        f"You're: {request.user.name} "
        f"with `user_id` = {request.user.id}"
    )
    return WSGIResponse(status, headers, body)
