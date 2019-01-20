import sys 
from exceptions import InvalidUsername, NotLoggedInError, NotPermittedError
from authenticator import Authenticator
from user import User

import pdb

#pdb.set_trace()

class Authorizor:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name):
        '''Create a new permission that users
         can be added to'''
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission already exists")

    def permit_user(self, perm_name, username):
        '''Grant the given permission to the user'''
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername("user {} does not exist".format(username))
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        #print(self.authenticator.is_logged_in(username), '-->', perm_name, username, self.authenticator.users[username].__dict__)
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True

#autenticador = Authenticator()
#miautorizador = Authorizor(autenticador)

#autenticador.add_user("joe", "joepassword")
#print(autenticador.users["joe"].__dict__)
#miautorizador.add_permission("paint")
#miautorizador.permit_user("paint", "joe")
#miautorizador.check_permission("paints", "joe")
#autenticador.login("joe", "joepassworda")
#miautorizador.check_permission("paint", "joe")
#print(autenticador.is_logged_in("joe"))
#miautorizador.check_permission("paints", "joe")
#print(autenticador.__dict__, miautorizador.__dict__)


