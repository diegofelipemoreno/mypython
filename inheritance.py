import pdb

#pdb.set_trace()

class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest

class ContactList(list):
    def search(self, name):
        '''Return all contacts that contain the search value
           in their name.'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                #pdb.set_trace()
                matching_contacts.append(contact)
        #print(matching_contacts)
        return matching_contacts

class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we send "
              "{} order to {}".format(order, self.name))

class Friend(Contact):
    def __init__(self, name, email, phone)
        super().__init__(name, email)
        self.phone = phone


c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johnb@example.net")
c3 = Contact("Jenna C", "jennac@example.net")
[c.name for c in Contact.all_contacts.search('John')]
#Contact.all_contacts.search('John A')
longkeys = LongNameDict()
longkeys['hello'] = 1
longkeys['longest yet'] = 5
longkeys['hello2'] = 'world'
longkeys.longest_key()

