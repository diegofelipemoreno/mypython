import sys 
from authenticator import Authenticator
from user import User

import pdb

#pdb.set_trace()

class auth_user:
    def __init__(self):
        mytest = User('diego', 'mypassword')
        mytest.update(Authenticator())

yo = auth_user()
print(yo.__dict__)
