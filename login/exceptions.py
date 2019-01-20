import pdb

#pdb.set_trace()

class AuthException(Exception):
    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user

class UsernameAlreadyExists(AuthException):
    pass

class PasswordTooShort(AuthException):
    def __init__(self, AuthException):
        return None

class InvalidUsername(AuthException):
    def __init__(self, AuthException):
        return None

class InvalidPassword(AuthException):
    pass

class NotLoggedInError(AuthException):
    pass

class NotPermittedError(AuthException):
    pass