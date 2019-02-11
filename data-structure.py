import pdb
import datetime
from collections import namedtuple
from collections import defaultdict
import string

# Object
o = object()
#o.x = 5
# Error slots to save data 
#print(o)x

class MyObject():
    pass

m = MyObject()
m.x = "hello"
#print(m , m.x)

stock = "Goog", 613.30, 625.86, 610.50
stock2 = ("goog", 613, 625.86, 610.50)

#print(stock2)


def middle(stock, date):
    symbol, current, high, low = stock
    return (((high + low) / 2), date)

mid_value, date = middle(("Goog", 613.30, 625.30, 610.50), datetime.date(2010, 1, 6))

#print(mid_value, date)

high = stock[2]

print(stock[1:3])
print(stock)

# --------------------------- TUPLES -----------------------------
# great to deal with read-only data. They are inmutable
Stocks = namedtuple("Stocks", "symbol current hight low")
stocks = Stocks("Goog", 613.30, hight=625.86, low=610.50)

print(">>>>>>>>>>>>>")
print(stocks)


# ------------------------ DICTIONARIES -------------------------
print(">>>>>>>>>>>>>")
mystocks = { "Goog": (613.30, 625.86, 610.50),
             "MSFT": (30.25, 30.70, 30.19) }
print(mystocks)
print(mystocks.setdefault("ASO", "OSO"), "-->")
print(mystocks)
print(mystocks.keys())
print(mystocks.values())

for stock, values in mystocks.items():
    print("{} last value is {}".format(stock, values[0]))

mystocks["ASO"] = "REPLACED"
print(mystocks)
print(">>>>>>>>>>>>>")

random_keys = {}
random_keys["astring"] = "somestring"
random_keys[5] = "aninteger"
random_keys[25.2] = "float work too"
random_keys[("abc", 123)] = "so do tuples"

print(random_keys)

class AnObject:
    def __init__(self, avalue):
        self.avalue = avalue

my_object = AnObject(14)
random_keys[my_object] = "We can even store objects"
my_object.avalue = 12

try:
    random_keys[[1,2,3]] = "We can`t store lists though"
except:
    print("uanble to store list \n")

print(my_object.__dict__, random_keys)
print(">>>>>>>>>>>>>")
for key, value in random_keys.items():
    print("{} has value {}".format(key, value))
print(">>>>>>>>>>>>>")
def letter_frequence(sentence):
    frequencies = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1
    return frequencies

print(letter_frequence('coquito'))

print(">>>>>>>>>>>>>")
def letter_frequencedos(sentence):
                  # Deja el default valor que se pasa en constructor
                  # en este caso int, puede ser una lista, list. Etc
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies 

print(letter_frequencedos('coquito'))

print(">>>>>>>>>>>>>")
# ---------- CUSTOM defaultdict -------------------

num_items = 0
def tuple_counter():
    global num_items
    num_items += 1
    return (num_items, [])

d = defaultdict(tuple_counter)
d['a'][1].append("hello")
d['b'][1].append("world")
print(d)

# --------------------- LISTS -----------------------------

CHARACTERS = list(string.ascii_letters) + [" "]

def letter_frequency(sentence):
    frequencies = [(c, 0) for c in CHARACTERS]
    for letter in sentence:
        index = CHARACTERS.index(letter)
        frequencies[index] = (letter, frequencies[index][1] + 1)
    return frequencies

print(letter_frequency('coquito'))


# --------------------- SORTING LISTS -----------------------------

class WeirdSortee:
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string
    
    def __repr__(self):
        return "{}:{}".format(self.string, self.number)

a = WeirdSortee('a', 4, True)
b = WeirdSortee('b', 3, True)
c = WeirdSortee('c', 2, True)
d = WeirdSortee('d', 1, True)
l = [a,b,c,d]
print(">>>>>>>>>>>>>")
print(l.sort())

print(">>>>>>>>>>>>>")
x = [(1, 'c'), (2, 'a'), (3, 'b')]
x.sort()
print(x)
x.sort(key=lambda i: i[1])
print(x)
print(">>>>>>>>>>>>>")
l = ["hello", "HELP", "Helo"]
l.sort()
l.sort(key=str.lower)


# -------------------------- SETS -----------------------------

