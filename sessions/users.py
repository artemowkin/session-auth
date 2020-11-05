class BaseUser:

    """Base class for users"""

    pass


class AnonymousUser(BaseUser):

    """Unauthenticated (anonymous) user object

    Attributes
    ----------
    self.id : int
        Id of anonymous user is 0
    self.name : str
        Name of anonymous user is 'anonymous_user'

    """

    def __init__(self) -> None:
        self.id = 0
        self.name = 'anonymous_user'


class User(BaseUser):

    """Authenticated user object

    Attributes
    ----------
    self.id : int
        User id. This field is first in `fields` initial parameter
    self.name : str
        User name. This field is second in `fields` initial parameter

    """

    def __init__(self, fields) -> None:
        self.id = fields[0]
        self.name = fields[1]
