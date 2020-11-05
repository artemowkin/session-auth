from typing import Any

from sessions.users import AnonymousUser, BaseUser
from sessions.backends import get_user_by_session_id


class WSGIRequest:

    """Request object to work with `environ` variables

    Attributes
    ----------
    path : str
        Requested path
    method : str
        Method of request
    cookies : dict
        Cookies from request
    user : User
        User object

    Methods
    -------
    get_full_path()
        Returns full requested path

    """

    def __init__(self, environ: dict) -> None:
        self._environ = environ

    @property
    def path(self) -> str:
        """Property that returns `PATH_INFO` environ variable"""
        return self._environ.get('PATH_INFO', '')

    @property
    def method(self) -> str:
        """Property that returns `REQUEST_METHOD` environ variable"""
        return self._environ.get('REQUEST_METHOD', '')

    @property
    def cookies(self) -> dict:
        """
        Cached property. Parsed cookies from `HTTP_COOKIE` environ variable
        """
        if hasattr(self, '_cookies'):
            return self._cookies

        cookies = self._environ.get('HTTP_COOKIE', '')
        if not cookies:
            self._cookies = {}
        else:
            cookies_dict = dict(
                [cookie.split('=') for cookie in cookies.split('; ')]
            )
            self._cookies = cookies_dict

        return self._cookies

    @property
    def user(self) -> BaseUser:
        """
        Cached property. AnonymousUser if user isn't authenticated.
        Else User
        """
        if hasattr(self, '_user'):
            return self._user

        sessionid = self.cookies.get('sessionid', '')
        if not sessionid:
            self._user = AnonymousUser()
        else:
            self._user = get_user_by_session_id(sessionid)

        return self._user

    def get_full_path(self) -> str:
        """Return full requested path with GET-parameters"""
        return self._environ.get('RAW_URI', '')
