import sys
from agent import Agent
from mixins import get_valid_custom_input

import pdb

#pdb.set_trace()

class Menu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self):
        self.agent = Agent()
        self.choices = {
            "1": self.agent.list_properties,
            "2": self.agent.display_properties,
            "3": self.search_properties,
            "4": self.agent.add_property,
            "5": self.quit
            }

    def display_menu(self):
        print("""
    Notebook Menu
    1. Show list properties
    2. Show details properties
    3. Search by properties
    4. Add property
    5. Quit
""")

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input(PROMPT_MESSAGE["enter_option"])
            action = self.choices.get(choice)
            if action: 
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def search_properties(self):
        list_properties = self.agent.list_properties()
        matching_properties = []
        payment_type = get_valid_custom_input(PROMPT_MESSAGE["payment_type"], ("rental", "purchase", "none"))
        property_type = get_valid_custom_input(PROMPT_MESSAGE["property_type"], ("house", "apartment", "none"))
        querySring = ''

        if (property_type.lower() != 'none'):
            querySring += property_type.capitalize()

        if (payment_type.lower() != 'none'):
            querySring += payment_type.capitalize()

        for value in list_properties:

            if querySring and querySring in str(value.__class__.__name__): 
                matching_properties.append(value)

        print(matching_properties)
    
    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)

'''Prompt text messages'''
PROMPT_MESSAGE = {
    "enter_option": "Enter an option: ",
    "property_type": "What type of property? ",
    "payment_type": "What payment type?  "
}

if __name__ == "__main__":
    Menu().run()