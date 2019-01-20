import sys 
from exceptions import InvalidUsername, PasswordTooShort, InvalidPassword, NotLoggedInError, NotPermittedError
from authenticator import Authenticator
from authorizor import Authorizor

import pdb

#pdb.set_trace()

class Editor:
    autenticador = Authenticator()
    miautorizador = Authorizor(autenticador)

    def __init__(self):
        self.username = None
        self.menu_map = {
            "1": self.login,
            "2": self.add_user,
            "3": self.add_permision,
            "4": self.is_permitted,
            "5": self.permit_user,
            "6": self.quit
        }

    def add_permision(self):
        perm_name = input("Permision: ")
       
        try:
            Editor.miautorizador.add_permission(perm_name)
        except PermissionError as exception:
            print(exception)

    def permit_user(self):
        perm_name = input("Permision: ")
        username = input("User name: ")
        
        try:
            Editor.miautorizador.permit_user(perm_name, username)
        except PermissionError as exception:
            print(exception)
        except InvalidUsername as exception:
            print(exception)
        

    def add_user(self):
        username = input("username: ")
        password = input("password: ")

        try:
            Editor.autenticador.add_user(username, password)
        except PasswordTooShort as exception:
            print("The password from user {} is too short".format(exception))

    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = Editor.autenticador.login(username, password)
            except InvalidUsername:
                print("Sorry, that username does not exist")
            except InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username

    def is_permitted(self):
        is_perm = False
        while not is_perm:
            perm_name = input("Permission: ")
            try:
                is_perm = Editor.miautorizador.check_permission(perm_name, self.username)              
            except NotLoggedInError as e:
                if e.username == None:
                    print("There is no an user logged, you shoul login in")
                else:
                    print("{} is not logged in".format(e.username))
                return False
            except NotPermittedError as e:
                print("{} cannot {}".format(e.username, perm_name))
                return False
            else:
                print("{} can {}".format(self.username, perm_name))
                return True

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ""
            while True:
                print("""
                    Please enter a command:
                    1. Login
                    2. Add user
                    3. Add permision
                    4. Check permision
                    5. Permit user
                    6. Quit
                    """)
                answer = input("enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                       print("{} is not a valid option".format(
                           answer))
                else:
                    func()
        finally:
            print("Thank you for testing the auth module")


myeditor = Editor()
#autenticador.add_user("joe", "joepass")
#autenticador.add_user("poe", "poepass")
#autenticador.login("joe", "joepass")
#miautorizador.add_permission("paint")
#myeditor.login()
#myeditor.is_permitted()
#print(autenticador.users["joe"].__dict__, autenticador.users["poe"].__dict__)
#print(autenticador.users["poe"].__dict__)
#print(InvalidUsername)
#print(autenticador.__dict__)
Editor().menu()
