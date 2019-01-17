import sys 
from house import House
from purchase import Purchase
import pdb

#pdb.set_trace()

class HousePurchase(Purchase, House):
    '''Represent a house purchase object.'''
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        
        return init


#Sets the prompt to set de values
#init = HousePurchase.prompt_init()
#print(init)

#with the data setted, instance a object and sets
# the data(**) by the constructor 
#house = HousePurchase(**init)
#print(house.__dict__, '--->')

#show data for a purchase house
#house.display()