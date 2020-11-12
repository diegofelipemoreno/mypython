import pdb
import shutil
import os
import datetime
import time
import sys
from collections import namedtuple
import shutil
import os.path

#Built in Functions

lenvar_list = len([1, 2, 3, 4])
myobj = {'a': 1, 'b': 2, 'c': 3}
lenvar_dict = len(myobj)
# LEN Counts the number of object in a dictionary or a list
print lenvar_list
print lenvar_dict
print myobj, 'myobj', myobj.__len__(), myobj.__getattribute__
print '------------------------'


# Reserve create a copy of the sequence that we set as parameter.
my_normal_list = [1, 2, 3, 4, 5]

class CustomSequence():
  def __len__(self):
    return 5

  def __getitem__(self, index):
    return 'x{0}'.format(index)

class FunkyBackwards():
  def __reversed__(self):
    return 'BACKWARDS!!!'

for seq in my_normal_list, CustomSequence(), FunkyBackwards():
  print ("\n{}: ".format(seq.__class__.__name__), "", seq)
  for item in reversed(seq):
    print(item, ", ")
print '------------------------'


# Enumerate creates a tuple here the first item ins the index and the second the object item
'''
import sys
filename = sys.argv[1]

with open(filename) as file:
  for index, line in enumerate(file):
    print("{0}: {1}".format(index + 1, line), "")
'''

my_dict = {"a": "oso", "b": "perro", "c": "casa"}
for index, line in enumerate(my_dict):
  print("{0}: {1}".format(index + 1, line), "")

print enumerate(my_dict)
print '------------------------'

# Zip Takes 2 or more sequences and creates a new sequence of tuples. 
list_one = ['a', 'b', 'c']
list_two = [1, 2, 3]
list_three = ['casa', 'perro', 'gato']
zipped = zip(list_one, list_two, list_three)
zipped = list(zipped)
unzipped = zip(*zipped)
print zipped
print unzipped
print '------------------------'

# Sorted takes an iterable input and return a list of elements sorted the difference with
# sort() is that it takes all iterables not just lists.

# A lambda function can take any number of arguments, but can only have one expression.
'''
EXAMPLE LAMBDA
Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))
'''

def min_max_indexes(seq):
  minimum = min(enumerate(seq), key=lambda s: s[1])
  maximum = max(enumerate(seq), key=lambda s: s[1])
  #print minimum
  #print maximun
  #x = lambda s: s[1]
  #print enumerate(seq), x(seq)
  return minimum[0], maximum[0]

a_list = [5, 0, 1, 4, 6, 3]
print min_max_indexes(a_list)
print min(a_list) 
print max(a_list) 
print '------------------------'


#List comprehensions, make some code lines in a single one
input_strings = ["1", "5", "28", "131", "3"]
output_integers = [int(num) for num in input_strings]
print output_integers
print '------------------------'

#Set and dictionary comprehensions
# namedtuple = The standard tuple uses numerical indexes to access its members.

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

fantasy_types = { b.title: b for b in books if b.genre == 'fantasy' }

# returns Book(author='Pratchett', title='Nightwatch', genre='fantasy')
print books
print '------------------------'
print fantasy_types
print '------------------------'


# Generators: It's a way to process a sequence without crating a set, list, object on memory. Saves memory for the machine.
# On this example is "(l for l in infile if 'WARNING' in l)"


try:
  inname =  sys.argv[1]
  outname = sys.argv[2]

  def warnings_filter(insequence):
    for l in insequence:
        if 'WARNING' in l:
          yield l.replace('\tWARNING', '')

  with open(inname) as infile:
    with open(outname, "w") as outfile:
      # warnings = (l for l in infile if 'WARNING' in l)
      # warnings = (l.replace('\tWARNING', '') for l in infile if 'WARNING' in l)
      # for l in infile:
      #   if 'WARNING' in l:
      #     outfile.write(l.replace('WARNING', ''))
      #     outfile.write(l)
      filter = warnings_filter(infile)
      for l in filter:
        outfile.write(l)
except:
    print("Need infile-asset.txt and outfile-asset.txt as sys parameters \n")


print '------------------------'
# alternative to method overloading
number = 5

def funky_function(number=number):
  print(number)

number = 6
funky_function(8)
funky_function()
print number
print '------------------------'

def hello(b=None):
  if b == None:
    b = []
  
  b.append('a')
  print(b)

hello()
hello()
print '------------------------'

# Variable argument lists:
# - The *links says "I'll accept any number of arguments and put them all in a list of strings named links". 
# - These arrive into the function as a dictionary. They are specified with two asterisks (as in **kwargs) 
# DEFAULT OPTIONS

class Options:
  default_options = {
    'port': 21,
    'host': 'localhost',
    'username': None,
    'password': None,
    'debug': False
  }

  def __init__(self, **kwargs):
    self.options = dict(Options.default_options)
    self.options.update(kwargs)

  def __getitem__(self, key):
    return self.options[key]

options = Options(username="dusty", password="drowssap", debug=True)

print options.__dict__
print '------------------------'


def augmented_move(target_folder, verbose=False, *filenames, **specific):
  '''Movel al filenames into the target_folder, allowing specific tratmente of certain files.'''
  print specific
  print filenames
  def print_verbose(message, filename):
    '''Print the message only if verbose is enabled'''
    if verbose:
      print message.format(filename)

  for filename in filenames:
    target_path = os.path.join(target_folder, filename)
    if filename in specific:
      if specific[filename] == 'ignore':
        print_verbose("Ignoring {0}", filename)
      elif specific[filename] == "copy":
        print_verbose("Copying {0}", filename)
        shutil.copy(filename, target_path)
    else:
      print_verbose("Moving {0}", filename)
      shutil.move(filename, target_path)

augmented_move("move_here", True, "four", "five", four="ignore", five="ignore")
print '------------------------'

#Unpacking arguments
def show_args(arg1, arg2, arg3="THREE"):
  print arg1, arg2, arg3

some_args = range(3) # = [0, 1, 2] 
more_args = {"arg1": "ONE", "arg2": "TWO"}

print ("Unpacking a sequence:")
show_args(*some_args)
print ("Unpacking a dict:")
show_args(**more_args)

print '------------------------'

#Functions are objects too

def my_function():
  print "The function was called"
my_function.description = "A silly function"

def second_function():
  print "The second was called"
second_function.description = "A sillier function"

def another_function(function):
  print "The description:"
  print function.description
  print "The name:"
  print function.__name__
  print "The class: "
  print function.__class__
  print "Now I'll call the function passed in"
  function()

another_function(my_function)
another_function(second_function)

print '------------------------'

class TimedEvent:
  def __init__(self, endtime, callback):
    self.endtime = endtime
    self.callback = callback

  def ready(self):
    return self.endtime < datetime.datetime.now()

class Timer:
  def __init__(self):
    self.events = []

  def call_after(self, delay, callback):
    end_time = datetime.datetime.now() + datetime.timedelta(seconds=delay)
    self.events.append(TimedEvent(end_time, callback))

  def run(self):
    while True:
      ready_events = (e for e in self.events if e.ready())
      for event in ready_events:
        event.callback(self)
        self.events.remove(event)
      time.sleep(0.5)

def format_time(message, *args):
  now = datetime.datetime.now().strftime("%I:%M:%S")
  print(message.format(*args, now=now))

def one(timer):
  format_time("{now}: Called One")

def two(timer):
  format_time("{now}: Called Two")

def three(timer):
  format_time("{now}: Called Three")

class Repeater:
  def __init__(self):
    self.count = 0
  def repeater(self, timer):
    format_time("{now}: repeat {0}", self.count)
    timer.call_after(5, self.repeater)

timer = Timer()
timer.call_after(1, one)
timer.call_after(2, one)
timer.call_after(2, two)
timer.call_after(4, two)
timer.call_after(3, three)
timer.call_after(6, three)
repeater = Repeater()
timer.call_after(5, repeater.repeater)
format_time("{now}: Starting")
#timer.run()

print '------------------------'

#Using functions as attributes (Monkey-patching)

class A:
  def prints(self):
    print("my class is A")

def fake_print():
  print("my class is not A")

a = A()
a.prints()
a.prints = fake_print
a.prints()

# Callable objects:
# So, the __init__ method is used when the class is called to initialize the instance,
# while the __call__ method is called when the instance is called
'''
  class Foo:
      def __init__(self, a, b, c):
          # ...

  x = Foo(1, 2, 3) # __init__


  class Foo:
      def __call__(self, a, b, c):
          # ...

  x = Foo()
  x(1, 2, 3) # __call__
'''

class Repeater:
  def __init__(self):
    self.count = 0

  def __call__(self, timer):
    format_time("{now}: repeat {0}", self.count) 
    self.count += 1
    timer.call_after(5, self) # It calls itself