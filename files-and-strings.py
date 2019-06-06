a = "HEllo"
b = "world"
c = ''' a multiple 
line string'''
d = """More 
multiple"""
e = ("Three " "Strings " 
        "Together")

s = "hello world"
s.startswith("hi")


emails = ("a@example.com", "b@example.com")
message = {
 'emails': emails,
 'subject': "You Have Mail!",
 'message': "Here's some mail for you!"
 }
template =  """
From: <{0[emails][0]}>
To: <{0[emails][1]}>
Subject: {0[subject]}
{0[message]}"""

print(template.format(message))
print("-"*30)

class Email:
    def __init__(self, from_addr, to_addr, subject, message):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.subject = subject
        self.message = message

email = Email("a@example.com", "b@example.com", "You have Mail!", "Here`s some mail for you!")
template ="""
From: <{0.from_addr}>
To: <{0.to_addr}>
Subject: {0.subject}

{0.message}"""

print(template.format(email))
print("-"*30)

subtotal = 12.32
tax = subtotal * 0.07
total = subtotal + tax

print("Sub: ${0:0.2f} Tax: ${1:0.2f} "
      "Total: ${total: 0.2f}".format(
          subtotal, tax, total=total
      ))

print("-"*30)

orders = [("burger", 2, 5),
          ("fries", 3.5, 1),
          ("cola", 1.75, 3)]

print("PRODUCT  QUANTITY    PRICE   SUBTOTAL")
for product, price, quantity in orders:
    subtotal = price * quantity
    print("{0:10s}{1:^9d}   ${2: <8.2f}${3: >7.2F}".format(
        product, quantity, price, subtotal)) 

print("-"*30)

#---------- Converting bytes to text ------------------

characters = "cliché"
print(characters.encode("UTF-8"))