import sys 
from mixins import get_valid_type_input, get_valid_custom_input
import pdb

#pdb.set_trace()

class Rental():
    '''Represent a rental object.'''
    prompt_init = ''

    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        '''initialize a note with furnished, utilities, rent tags.'''
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    def display(self):
        super().display()
        print()
        print(PROMPT_MESSAGE["purchase_details"])
        print(PROMPT_MESSAGE["furnished"], self.furnished)
        print(PROMPT_MESSAGE["utilities"], self.utilities)
        print(PROMPT_MESSAGE["rent"], self.rent)
        print()
    
    def prompt_init():
        return dict(furnished = get_valid_custom_input(PROMPT_MESSAGE["furnished"], ("yes", "no")),
                utilities = get_valid_type_input(PROMPT_MESSAGE["utilities"], "numbers"),
                rent = get_valid_type_input(PROMPT_MESSAGE["rent"], "number"))
    
    #is ready to be called for initialize this class from a child Class
    prompt_init = staticmethod(prompt_init)


'''Prompt text messages'''
PROMPT_MESSAGE = {
    "purchase_details": "RENTAL DETAILS",
    "furnished": "Furnished: ",
    "utilities": "Utilities: ",
    "rent": "Rent: "
}

#myrental = Rental()
#myrental.prompt_init()
#myrental.display()
