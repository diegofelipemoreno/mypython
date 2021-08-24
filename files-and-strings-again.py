import random, string

s = "hello world"
s.startswith('hi')
s.endswith('ld')
s.find('l')
s.index('l')

template = """
   public class {0} {{
       public static void main(String[] args) {{
           System.out.println({1});
}} }}"""
print(template.format("MyClass", "print('hello world')"));

print("-"*30)

class Email:
    def __init__(self, from_addr, to_addr, subject, message):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.subject = subject
        self.message = message

email = Email("a@example.com", "b@example.com", "you have an email", "Here's some mail for you")

template = """
{0}
From: <{0.from_addr}>
To: <{0.to_addr}>
Subject: {0.subject}

{0.message}
"""
print(template.format(email))
print("-"*30)

subtotal = 12.32
tax = subtotal * 0.07
total = subtotal + tax

print("Sub: ${0:0.2f} Tax: ${1:0.2f} "
            "Total: ${total: 0.2f}".format(subtotal, tax, total=total)
)
print("-"*30)

characters = b'\x63\x6c\x69\x63\x68\xe9'
print(characters)
print(characters.decode("latin-1"))
my_characters = "cliché"
print(my_characters.encode("UTF-8"))
print(my_characters.encode("latin-1"))
print(my_characters.encode("CP437"))
#print(my_characters.encode("ascii"))

print("-"*30)

class StringJoiner(list):
    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.result = "".join(self)

with StringJoiner() as joiner:
    for i in range(15):
        joiner.append(random.choice(string.ascii_letters))

print(joiner.result)
print("-"*30)

# coding=utf-8
from io import StringIO, BytesIO

source_file = StringIO("an oft-repeated cliché") 
dest_file = BytesIO()
char = source_file.read(1)

while char:
    dest_file.write(char.encode("ascii", "replace"))
    char = source_file.read(1)
print(dest_file.getvalue())
print("-"*30)


# PICKLE
import pickle

some_data = ["a list", "containing", 5, "values including another list", ["inner", "list"]]

with open("pickled_list", "wb") as file:
    pickle.dump(some_data, file)

with open("pickled_list", "rb") as file:
    loaded_data = pickle.load(file)


print(loaded_data)
assert loaded_data == some_data