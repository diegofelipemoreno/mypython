import sys 
from mixins import get_valid_type_input
import pdb

#pdb.set_trace()

class Property:
    '''Represent a Property object.'''
    def check_if_prompt_init(self):
        args_string = ''

        for attr, value in vars(self).items():
            args_string += str(value)

        if (not args_string):
            self.prompt_init()

    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        '''initialize a note with square feet, number bedrooms, number bathrooms tags.'''
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.beds = beds
        self.baths = baths
        #self.check_if_prompt_init()

    def display(self):
        '''return all property tag'''
        print()
        print(PROMPT_MESSAGE["property_details"])
        print(PROMPT_MESSAGE["title_line"])
        print(PROMPT_MESSAGE['square_footage'], "{}".format(self.square_feet))
        print(PROMPT_MESSAGE["beds"], "{}".format(self.beds))
        print(PROMPT_MESSAGE["baths"], "{}".format(self.baths))

    def prompt_init():
        return dict(square_feet = get_valid_type_input(PROMPT_MESSAGE["input_square"], "number"),
                beds = get_valid_type_input(PROMPT_MESSAGE["input_bedrroms"], "number"),
                baths = get_valid_type_input(PROMPT_MESSAGE["input_baths"], "number"))

    #is ready to be called for initialize this class from a child Class example (apartment)
    prompt_init = staticmethod(prompt_init)


'''Prompt text messages'''
PROMPT_MESSAGE = {
    "baths": "bathrooms: ",
    "beds": "bedrooms: ",
    "input_baths": "Enter number of baths: ",
    "input_bedrroms": "Enter number of bedrooms: ",
    "input_square": "Enter the square feet: ",
    "property_details": "PROPERTY DETAILS",
    "square_footage": "square footage: ",
    "title_line": "================"
}

#myproperty = Property()
#myproperty.prompt_init()
#myproperty.display()
#get_valid_type_input(3, 'number')

