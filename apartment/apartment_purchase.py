import sys 
from apartment import Apartment
from purchase import Purchase
import pdb

#pdb.set_trace()

class ApartmentPurchase(Purchase, Apartment):
    '''Represent a apartment Purchase object.'''
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        
        return init


#Sets the prompt to set de values
#init = ApartmentPurchase.prompt_init()
#print(init)

#with the data setted, instance a object and sets
# the data(**) by the constructor 
#apartment = ApartmentPurchase(**init)
#print(Apartment.__dict__, '--->')

#show data for a Purchase Apartment
#apartment.display()