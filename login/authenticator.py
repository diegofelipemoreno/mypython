import sys 
from exceptions import UsernameAlreadyExists, PasswordTooShort, InvalidPassword, InvalidUsername
from user import User

import pdb

#pdb.set_trace()

class Authenticator:
    def __init__(self):
        '''Construct an authenticator to manage
           users logging in and out.'''
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooShort(username)

        self.users[username] = User(username, password)

    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)
        
        if not user.check_password(password):
            raise InvalidPassword(username, user)
        
        user.is_logged_in = True

        return True
    
    def is_logged_in(self, username):
        if username in self.users:
            #print(username, self.users[username].__dict__)
            return self.users[username].is_logged_in
        return False

    def show_users():
        print(self.users)



