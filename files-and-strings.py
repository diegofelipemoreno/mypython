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