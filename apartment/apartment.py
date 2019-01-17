import sys 
from property import Property
import sys 
from mixins import get_valid_custom_input
import pdb

#pdb.set_trace()

class Apartment(Property):
    '''Represent a Apartment object.'''
    prompt_init = ''
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        '''initialize a note with square feet, number bedrooms, number bathrooms tags.'''
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print(PROMPT_MESSAGE["apartment_details"])
        print(PROMPT_MESSAGE["laundry"], self.laundry)
        print(PROMPT_MESSAGE["balcony"], self.balcony)

    def prompt_init():
        parent_init = Property.prompt_init()        
        laundry = get_valid_custom_input(PROMPT_MESSAGE["laundry_input"], Apartment.valid_laundries) or ''
        balcony = get_valid_custom_input(PROMPT_MESSAGE["balcony_input"], Apartment.valid_balconies) or ''

        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        print(parent_init, '-->')
        
        return parent_init

    #is ready to be called for initialize this class from a child Class
    prompt_init = staticmethod(prompt_init)


'''Prompt text messages'''
PROMPT_MESSAGE = {
    "apartment_details": "APARTMENT DETAILS",
    "balcony_input": "Does the property have a balcony?",
    "balcony": "has balcony: ",
    "laundry_input": "What laundry facilities does the property have?",
    "laundry": "laundry: "
}

myapartment = Apartment()
myapartment.prompt_init()
#myapartment.display()
#get_valid_input("what laundry?", ("coin", "ensuite", "none"))