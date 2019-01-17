import sys 
from mixins import get_valid_custom_input
from house_rental import HouseRental
from house_purchase import HousePurchase
from apartment_rental import ApartmentRental
from apartment_purchase import ApartmentPurchase

import pdb

#pdb.set_trace()

class Agent:
    '''Represent a Agent class.'''
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
        }
    
    type_property = ("house", "apartment")
    type_contract = ("rental", "purchase")

    def __init__(self):
        '''Initialize a agent'''
        self.propertyList = []

    def list_properties(self):
        '''list all properties'''
        print(self.propertyList)
        return self.propertyList

    def display_properties(self):
        '''list property properties'''
        for property in self.propertyList:
            property.display()
            print()
            print(PROMPT_MESSAGE["separator"])
            print()

    def add_property(self):
        property_type = get_valid_custom_input(PROMPT_MESSAGE["property_type"], Agent.type_property)
        payment_type = get_valid_custom_input(PROMPT_MESSAGE["payment_type"], Agent.type_contract)

        PropertyClass = self.type_map[(property_type, payment_type)]
        args_property = PropertyClass.prompt_init()
        current_property = PropertyClass(**args_property)
        self.propertyList.append(current_property)
        current_property.display()


'''Prompt text messages'''
PROMPT_MESSAGE = {
    "property_type": "What type of property? ",
    "payment_type": "What payment type?  ",
    "separator": "================ ================"
}

#myagent = Agent()
#myagent.add_property()
#myagent.list_properties()
#myproperty.prompt_init()
#myproperty.display()
#get_valid_type_input(3, 'number')

