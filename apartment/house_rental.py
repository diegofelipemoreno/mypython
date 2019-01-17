import sys 
from house import House
from rental import Rental
import pdb

#pdb.set_trace()

class HouseRental(Rental, House):
    '''Represent a house rental object.'''
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        
        return init


#Sets the prompt to set de values
#init = HouseRental.prompt_init()
#print(init)

#with the data setted, instance a object and sets
# the data(**) by the constructor 
#house = HouseRental(**init)
#print(house.__dict__, '--->')

#show data for a rental house
#house.display()