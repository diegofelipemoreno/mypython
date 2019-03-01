import pdb
import sys
filename = sys.argv[1]

#pdb.set_trace()

normal_list = [1,2,3,4,5]
normal_list_letters = ['a', 'b', 'c', 'd', 'e']

class CustomSequence():
    def __len__(self):
        return 5
    
    def __getitem__(self, index):
        return "x{0}".format(index)

class FunkyBackwards(CustomSequence):
    def __reversed__(self):
        return "BACKWARDS!"

for seq in normal_list, CustomSequence(), FunkyBackwards():
    print("\n{}: ".format(seq.__class__.__name__), end="")
    for item in reversed(seq):
        print(item, end=", ")

print("\n\t")
print(">"*30)
# -------- REVERSE -----------
for item in reversed(normal_list):
    print(item)

print("-"*30)
# --------  ENUMERATE ----------- (creates a list of tuples)
for index, line in enumerate(normal_list_letters):
    print("{0}: {1}".format(index, line))

print("*"*30)
# --------  ZIP ----------- (2 more squences creates a tuple)
'''
contacts = []
with open(filename) as file:
    header = file.readline().strip().split('\t')

    for line in file:
        line = line.strip().split('\t')
        contact_map = zip(header, line)
        contacts.append(dict(contact_map))

for contact in contacts:
    print("email: {email} -- {last}, {first}".format(**contact))

list_one = ['a', 'b', 'c']
list_two = [1, 2, 3]
zipped = zip(list_one, list_two)
zipped = list(zipped)

print(zipped)

unzipped = zip(*zipped)
unzipped = list(unzipped)
print(unzipped)
print(">"*30)

# --------  SORTED ----------- maximum minimum numbers
def min_max_indexes(seq):
    minimum = min(enumerate(seq))
    maximum = max(enumerate(seq))
    print(minimum[0], maximum[0])
    return minimum[0], maximum[0]

alist = [5, 6, 1, 4, 0, 3]
min_max_indexes(alist)

# -------- All  ----------- all iterable elements are True(validation)
print("x"*30)

def all(seq):
    for element in seq:
        if element > 7:
            return False
        return True

print(all(alist))
print("-"*30)


# -------- List comprehensions  ----------- 
input_strings = ['1', '5', '28', '131', '3']
output_intergers = []

'''
'''
for num in input_strings:
    output_intergers.append(int(num))
'''
'''

output_intergers = [int(num) for num in input_strings]
output_ints = [int(n) for n in input_strings if int(n) < 50]

print(output_ints)

print("-"*30)

with open(filename) as file:
    header = file.readline().strip().split('\t')
    contacts = [ dict(
                    zip(header, line.strip().split('\t'))
                ) for line in file
               ]
print(contacts)


# ----------- Set and dictionary comprehensions -----------------
print("x"*30)

from collections import namedtuple

Book = namedtuple("Book", "author title genre")
books = [
 Book("Pratchett", "Nightwatch", "fantasy"),
 Book("Pratchett", "Thief Of Time", "fantasy"),
 Book("Le Guin", "The Dispossessed", "scifi"),
 Book("Le Guin", "A Wizard Of Earthsea", "fantasy"),
 Book("Turner", "The Thief", "fantasy"),
 Book("Phillips", "Preston Diamond", "western"),
 Book("Phillips", "Twice Upon A Time", "scifi")
]

fantasy_authors = {
    b.author for b in books if b.genre == 'fantasy'
}

fantasy_title = {
    b.title: b for b in books if b.genre == 'fantasy'
}

print(fantasy_title)
'''
# ----------- Generator expressions ----------------- 
# looping over items without final conatiner in order to save system memory
print("-"*30)

inname = sys.argv[1]
outname = sys.argv[2]
warnings = ()

with open(inname) as infile:
    with open(outname, "w") as outfile:
            for l in infile:
                if 'WARNING' in l:
                    warnings = (l)

                    for l in warnings:
                        outfile.write(l)