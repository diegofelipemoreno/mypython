import pdb
import datetime
from collections import namedtuple
from collections import defaultdict
import string
from collections import KeysView, ItemsView, ValuesView

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
print(">>>>>iiii>>>>>>")
l = ["hello", "HELP", "Helo"]
l.sort()
l.sort(key=str.lower)


# -------------------------- SETS -----------------------------

song_library = [("Phantom Of The Opera", "Sarah Brightman"),
 ("Knocking On Heaven's Door", "Guns N' Roses"),
 ("Captain Nemo", "Sarah Brightman"),
 ("Patterns In The Ivy", "Opeth"),
 ("November Rain", "Guns N' Roses"),
 ("Beautiful", "Sarah Brightman"),
 ("Mal's Song", "Vixy and Tony")]

artists = set()
for song, artist in song_library:
    artists.add(artist)

print(artists)
print(">>>>>>>>>>>>>")

for artist in artists:
    print("{} plays good music".format(artist))

print(">>>>>>>>>>>>>")

alphabetical = list(artists)
alphabetical.sort()
print(alphabetical)

print(">>>>>>>>>>>>>")

my_artists = {"Sarah Brightman", "Guns N' Roses",
 "Opeth", "Vixy and Tony"}
auburns_artists = {"Nickelback", "Guns N' Roses",
 "Savage Garden"}

print("All (UNION): {}".format(my_artists.union(auburns_artists)))
print("Both (intersection): {}".format(my_artists.intersection(auburns_artists)))
print("Either but not both: {}".format(my_artists.symmetric_difference(auburns_artists)))

print(">>>>>>>>>>>>>")

my_artists = {"Sarah Brightman", "Guns N' Roses",
 "Opeth", "Vixy and Tony"}
bands = {"Guns N' Roses", "Opeth"}

print("my_artists is to bands:")
print("issuperset: {}".format(my_artists.issuperset(bands)))
print("issubset: {}".format(my_artists.issuperset(bands)))
print("difference: {}".format(my_artists.issuperset(bands)))
print("*"*20)
print("bands is to my_artists:")
print("issuperset: {}".format(bands.issuperset(my_artists)))
print("issubset: {}".format(bands.issubset(my_artists)))
print("difference: {}".format(bands.difference(my_artists)))

# CHECK OBJECT PRIVATE METHODS
print(dir(list))

# HELP OBJECT METHOD HOW TO WORKS
#help(list.__add__)

# Sorted dictionary

class DictSorted(dict):
    def __new__(*args, **kwargs):
        new_dict = dict.__new__(*args, **kwargs)
        new_dict.ordered_keys = []
        return new_dict

    def __setitem__(self, key, value):
        ''' self[key] = value syntax'''
        if key not in self.ordered_keys:
            self.ordered_keys.append(key)
        super().__setitem__(key, value)

    def setdefault(self, key, value):
        if key not in self.ordered_keys:
            self.ordered_keys.append(key)
        return super().setdefault(key, value)

    def keys(self):
        return KeysView(self)

    def values(self):
        return ValuesView(self)
    
    def items(self):
        return ItemsView(self)
    
    def __iter__(self):
        ''' for x in self syntax '''
        return self.ordered_keys.__iter__()

print(">"*30)  
ds = DictSorted()
d = {}

ds['b'] = 2
ds['a'] = 1
ds.setdefault('c', 3)

d['b'] = 2
d['a'] = 1
d.setdefault('c', 3)

print(ds)
print(d)

for key, value in ds.items():
    print(key, value)