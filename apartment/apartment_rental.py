import sys 
from apartment import Apartment
from rental import Rental
import pdb

#pdb.set_trace()

class ApartmentRental(Rental, Apartment):
    '''Represent a apartment rental object.'''
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        
        return init


#Sets the prompt to set de values
#init = ApartmentRental.prompt_init()
#print(init)

#with the data setted, instance a object and sets
# the data(**) by the constructor 
#apartment = ApartmentRental(**init)
#print(Apartment.__dict__, '--->')

#show data for a rental Apartment
#apartment.display()