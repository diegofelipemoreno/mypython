import sys 
from mixins import get_valid_type_input
import pdb

#pdb.set_trace()

class Purchase():
    '''Represent a purchase object.'''
    prompt_init = ''

    def __init__(self, price='', taxes='', **kwargs):
        '''initialize a note with price, taxes tags.'''
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print()
        print(PROMPT_MESSAGE["purchase_details"])
        print(PROMPT_MESSAGE["price"], self.price)
        print(PROMPT_MESSAGE["taxes"], self.taxes)
        print()
    
    def prompt_init():
        return dict(price = get_valid_type_input(PROMPT_MESSAGE["price"], "number"),
                taxes = get_valid_type_input(PROMPT_MESSAGE["taxes"], "number"))
    
    #is ready to be called for initialize this class from a child Class
    prompt_init = staticmethod(prompt_init)


'''Prompt text messages'''
PROMPT_MESSAGE = {
    "purchase_details": "PURCHASE DETAILS",
    "price": "Selling price: ",
    "taxes": "Estimated taxes: "
}

#mypurchase = Purchase()
#mypurchase.prompt_init()
#mypurchase.display()
