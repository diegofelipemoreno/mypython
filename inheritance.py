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

class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we send "
              "{} order to {}".format(order, self.name))

class MailSender:
    def send_mail(self, message):
        print("sending mailt to " + self.email)

class EmailableContact(Contact, MailSender):
    pass

class AddressHolder():
    def __init__(self, addressDict):
        self.street = addressDict['street']
        self.city = addressDict['city']
        self.state = addressDict['state']
        self.code = addressDict['code']

class FullContact(Contact, AddressHolder):
    def __init__(self, name, email, AddressHolder):
        super().__init__(name, email)
        self.__dict__.update(AddressHolder.__dict__)
            

c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johnb@example.net")
c3 = Contact("Jenna C", "jennac@example.net")
f1 = Friend("Tommas", "tommas@example.net", "31342322",  {'phone': phone})
ad = { 'street': 'lupton street', 'city': 'bogota', 'state': 'cundinamarca', 'code': '123' }
#print(c3.__dict__, f1.__dict__)

e = EmailableContact("John Smith", "jsmith@example.net")
#(e.__dict__)
e.send_mail("Hello, test e-mail here")

aholder = AddressHolder(ad)
a = FullContact("Jenna C", "jennac@example.net", aholder)
print(a.__dict__)

#[c.name for c in Contact.all_contacts.search('John')]
#Contact.all_contacts.search('John A')
longkeys = LongNameDict()
longkeys['hello'] = 1
longkeys['longest yet'] = 5
longkeys['hello2'] = 'world'
longkeys.longest_key()

