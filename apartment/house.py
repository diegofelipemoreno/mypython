import sys 
from property import Property
import sys 
from mixins import get_valid_custom_input, get_valid_type_input
import pdb

#pdb.set_trace()

class House(Property):
    '''Represent a House object.'''
    prompt_init = ''
    valid_fenced = ("yes", "no")
    valid_garage = ("attached", "detached", "none")

    def __init__(self, num_stories='', garage='', fenced = '', **kwargs):
        '''initialize a note with num_stories, garage, fenced tags.'''
        super().__init__(**kwargs)
        self.num_stories = num_stories
        self.garage = garage
        self.fenced = fenced

    def display(self):
        super().display()
        print()
        print(PROMPT_MESSAGE["house_details"])
        print(PROMPT_MESSAGE["num_stories"], self.num_stories)
        print(PROMPT_MESSAGE["garage"], self.garage)
        print(PROMPT_MESSAGE["fenced"], self.fenced)
        print()
        
    def prompt_init():
        parent_init = Property.prompt_init()        
        num_stories = get_valid_type_input(PROMPT_MESSAGE["num_stories"], "number") or ''
        garage = get_valid_custom_input(PROMPT_MESSAGE["garage"], House.valid_garage) or ''
        fenced = get_valid_custom_input(PROMPT_MESSAGE["fenced"], House.valid_fenced) or ''

        parent_init.update({
            "num_stories": num_stories,
            "garage": garage,
            "fenced": fenced
        })
        #print(parent_init)
        return parent_init

    #is ready to be called for initialize this class from a child Class
    prompt_init = staticmethod(prompt_init)


'''Prompt text messages'''
PROMPT_MESSAGE = {
    "house_details": "HOUSE DETAILS",
    "num_stories": "Number stories: ",
    "garage": "Has garage: ",
    "fenced": "Fenced yard number: ",
}

#mycasa = House()
#mycasa.display()
#get_valid_input("what laundry?", ("coin", "ensuite", "none"))

#print(mycasa.__class__.__name__)