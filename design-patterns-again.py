import sys
import abc 
import sqlite3
from abc import ABC, abstractmethod 
from datetime import datetime

# DECORATOR PATTERN
# The decorator pattern allows us to "wrap" an object that provides core functionality with other objects that alter that functionality.

# Abstract class
class Beverage(ABC):
  @abstractmethod
  def get_description(self):
    pass

  @abstractmethod
  def get_cost(self):
    pass

class Coffee(Beverage):
  def get_description(self):
    return "Coffee"
  
  def get_cost(self):
    return 1

class LatteDecorator():
  def __init__(self, coffee):
    self.coffee = coffee

  def get_description(self):
    return self.coffee.get_description() + " Latte"
  
  def get_cost(self):
    return self.coffee.get_cost() + 2

class LatteSugarDecorator():
  def __init__(self, latte):
    self.latte = latte

  def get_description(self):
    return self.latte.get_description() + " with sugar"
  
  def get_cost(self):
    return self.latte.get_cost() + .5

class MockaDecorator():
  def __init__(self, coffee):
    self.coffee = coffee

  def get_description(self):
    return self.coffee.get_description() + " Mocka"
  
  def get_cost(self):
    return self.coffee.get_cost() + 3


coffee = Coffee()
latte = LatteDecorator(coffee)
mocka = MockaDecorator(coffee)
latte_with_sugar = LatteSugarDecorator(latte)

print(coffee.get_description(), coffee.get_cost())
print(latte.get_description(), latte.get_cost())
print(mocka.get_description(), mocka.get_cost())
print(latte_with_sugar.get_description(), latte_with_sugar.get_cost())
print("-"*30)


# OBSERVER PATTERN (Push -> Poll way)

# Observable
class Workstation:
  def __init__(self):
    self.observers = []
    self.isRaining = False

  def add(self, observer):
    self.observers.append(observer)

  def remove(self, observer):
    self.observers.remove(observer)

  def notify(self):
    for observer in self.observers:
      observer.update()

  def get_state(self):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    state_message = "Is Raining? {0}. At {1}:".format(self.isRaining, current_time)
    
    return state_message

# Observer
class PhoneDisplay:
  def __init__(self, station):
    self.station = station
  
  def update(self):
    print("PhoneDisplay", self.station.get_state())

# Observer
class TvDisplay:
  def __init__(self, station):
    self.station = station
  
  def update(self):
    print("TvDisplay", self.station.get_state())

ws = Workstation()
pd = PhoneDisplay(ws)
td = TvDisplay(ws)

ws.add(pd)
ws.add(td)
ws.remove(td)

ws.notify()
ws.notify()

print("-"*30)

# ITERATOR PATTERN: Way to access the elements to the algoritm object without caring about the type of structure.
# - You can iterate over any data structure colelction, list, array linked list etc
# - It gives you the posibility to ask for the next item on the list and evaluate it
# - You can know the current item position and move to next one or back one.

# Iterable -> Forest, House
# Iterator -> the way to iterate over this different structure collections.
#              forest.getIterator()
#               house.getIterator()
# Iterable constructs the iterator

inventory = [
  "sword",
  "shield",
  "spear",
  "gun",
  "axe"
]

class HandleHeldInventory:
  def __init__(self, inventory):
    self.inventory_list = inventory
    self.left_item = None
    self.right_item = None

  def set_handle_items(self, left, right):
    self.left_item = left
    self.right_item = right
    print(self.left_item, self.right_item)

  def get_iterator(self):
    return HandleHeldInventoryIterator(self)

class HandleHeldInventoryIterator:
  def __init__(self, handle_held_inventory):
    self.inventory_list = handle_held_inventory.inventory_list
    self.inventory_index = 0

  def is_done(self):
    return self.inventory_index < 0 or self.inventory_index + 1 == len(self.inventory_list)

  def next_item(self):
    if self.is_done():

      return ''
    else:
      self.inventory_index = self.inventory_index + 1

      return self.inventory_list[self.inventory_index]

  def previous_item(self):
    if self.inventory_index:
      self.inventory_index = self.inventory_index - 1

      return self.inventory_list[self.inventory_index]
    else:
      return self.inventory_list[self.inventory_index]

  def get_current_item(self):
    return self.inventory_list[self.inventory_index]

  def get_handle_items(self):
    index = self.inventory_index

    if self.is_done():
      return (self.inventory_list[index - 1], self.inventory_list[index])
    else:
      return (self.inventory_list[index], self.inventory_list[index + 1])

my_bag = HandleHeldInventory(inventory)
my_bag_iterator = my_bag.get_iterator()
#print(my_bag.__dict__)
#print(my_bag_inventory)

current_handle_items = my_bag_iterator.get_handle_items()
my_bag.set_handle_items(*current_handle_items)

my_bag_iterator.next_item()

current_handle_items = my_bag_iterator.get_handle_items()
my_bag.set_handle_items(*current_handle_items)

my_bag_iterator.next_item()

current_handle_items = my_bag_iterator.get_handle_items()
my_bag.set_handle_items(*current_handle_items)

my_bag_iterator.previous_item()

current_handle_items = my_bag_iterator.get_handle_items()
my_bag.set_handle_items(*current_handle_items)

my_bag_iterator.next_item()

current_handle_items = my_bag_iterator.get_handle_items()
my_bag.set_handle_items(*current_handle_items)

my_bag_iterator.next_item()

current_handle_items = my_bag_iterator.get_handle_items()
my_bag.set_handle_items(*current_handle_items)

my_bag_iterator.next_item()

current_handle_items = my_bag_iterator.get_handle_items()
my_bag.set_handle_items(*current_handle_items)

my_bag_iterator.previous_item()

current_handle_items = my_bag_iterator.get_handle_items()
my_bag.set_handle_items(*current_handle_items)

my_bag_iterator.previous_item()

current_handle_items = my_bag_iterator.get_handle_items()
my_bag.set_handle_items(*current_handle_items)

my_bag_iterator.previous_item()

current_handle_items = my_bag_iterator.get_handle_items()
my_bag.set_handle_items(*current_handle_items)

my_bag_iterator.previous_item()

current_handle_items = my_bag_iterator.get_handle_items()
my_bag.set_handle_items(*current_handle_items)

my_bag_iterator.previous_item()

current_handle_items = my_bag_iterator.get_handle_items()
my_bag.set_handle_items(*current_handle_items)

print("-"*30)


# STRATEGY PATTERN:
# Family of algoritms which each one of them are interchangeable. They are independent of the client that uses it.
# Choose the better way function to deal with some code where the Classes have
# the same methods name but deal with the data different way, depending what we
# need. COMPOSITION RATHER INHERITANCE

class Duck:
  def __init__(self, quackStrategy, flyStrategy):
    self.quack = quackStrategy
    self.fly = flyStrategy

class SimpleQuack:
  def __call__(self):
    return "Simple Quack"

class CustomQuack:
  def quack(self):
    return "Custom Quack"

class JetFly:
  def fly(self):
   return "Jet Fly"

class WingFly:
  def __call__(self):
    return "Wind Fly"

simple_quack = SimpleQuack()()
custom_quack = CustomQuack()
jet_fly = JetFly()
wing_fly = WingFly()()

cityDuck = Duck(SimpleQuack(), jet_fly.fly)
MountainDuck = Duck(custom_quack.quack, WingFly())

print("city Duck", cityDuck.quack(), cityDuck.fly()) 
print("mountain Duck", MountainDuck.quack(), MountainDuck.fly()) 

print("-"*30)

# STATE pattern: Reprsents a state-transition. It needs to have a:
# - Context Class / actions that has the state class.
# - Multiple Class States that according the context sends it change its state.
# Context Object behavies different depending his change state.
# It doesn't have memmory just acts according the action of the state.

# Subway example
'''
Actions       enter   onPayOK   onPayFailed
State
  closeGate   close   enter     close

  openGate    enter   enter     enter
'''

# Context Class 
class Gate:
  def __init__(self):
    self.state = CloseGateState(self)

  def on_change_state(self, gateState):
    self.state = gateState

  def on_pay(self):
    return self.state.pay()

  def on_enter(self):
    return self.state.enter()

  def on_pay_ok(self):
    return self.state.pay_ok()

  def on_pay_failed(self):
    return self.state.pay_failed()


# State Class 1
class OpenGateState:
  def __init__(self, gate):
    self.gate = gate
  
  def enter(self):
    closeGateState = CloseGateState(self.gate)
    self.gate.on_change_state(closeGateState)
    print("Now you can enter. Open gate state")

  def pay(self):
    closeGateState = CloseGateState(self.gate)
    self.gate.on_change_state(closeGateState)
    print("You paid the ticket. Open gate state")
  
  def pay_ok(self):
    openGateState = OpenGateState(self.gate)
    self.gate.on_change_state(openGateState)
    print("Ticket has been paid. Open gate state")
  
  def pay_failed(self):
    closeGateState = CloseGateState(self.gate)
    self.gate.on_change_state(closeGateState)
    print("The Ticket paid failed. Open gate state")

# State Class 2
class CloseGateState:
  def __init__(self, gate):
    self.gate = gate
  
  def enter(self):
    closeGateState = CloseGateState(self.gate)
    self.gate.on_change_state(closeGateState)
    print("The Ticket has not been paid. Close gate state")

  def pay(self):
    closeGateState = CloseGateState(self.gate)
    self.gate.on_change_state(closeGateState)
    print("You paid the ticket. Close gate state")
  
  def pay_ok(self):
    openGateState = OpenGateState(self.gate)
    self.gate.on_change_state(openGateState)
    print("The Ticket has been paid. Close Gate state")
  
  def pay_failed(self):
    closeGateState = CloseGateState(self.gate)
    self.gate.on_change_state(closeGateState)
    print("The Ticket paid failed. Close gate state")


camdem = Gate()

camdem.on_enter()
camdem.on_pay()
camdem.on_pay_failed()
camdem.on_enter()

print("-"*30)


# SINGLETON Pattern 
# Provides just one instance and it provides a global access to it. 
# (Static retrieves a single instance the first time and if you call 
# it again it will retrieve the same instance again).
# In Python the __new__ method ensures that only one instance is created.
# In Python could be useful create singletons for the state classes on the state pattern.

#(Python example)
class OneOnly:
  _singleton = None
  def __new__(cls, *args, **kwargs):
    if not cls._singleton:
      cls._singleton = super(OneOnly, cls).__new__(cls, *args, **kwargs)
    return cls._singleton

o1 = OneOnly()
o2 = OneOnly()

print(o1 == o2)

print("-"*30)


# TEMPLATE Pattern
# Is use when we have several tasks in common but not all so we put a base development
# for the common ones.
# You never get an instance of the template class, just is defined in the subclasses.

#(Python book example)
'''
conn = sqlite3.connect("sales.db")
conn.execute("CREATE TABLE Sales (salesperson text, "
 "amt currency, year integer, model text, new boolean)")
conn.execute("INSERT INTO Sales values"
 " ('Tim', 16000, 2010, 'Honda Fit', 'true')")
conn.execute("INSERT INTO Sales values"
 " ('Tim', 9000, 2006, 'Ford Focus', 'false')")
conn.execute("INSERT INTO Sales values"
 " ('Gayle', 8000, 2004, 'Dodge Neon', 'false')")
conn.execute("INSERT INTO Sales values"
 " ('Gayle', 28000, 2009, 'Ford Mustang', 'true')")
conn.execute("INSERT INTO Sales values"
 " ('Gayle', 50000, 2010, 'Lincoln Navigator', 'true')")
conn.execute("INSERT INTO Sales values"
 " ('Don', 20000, 2008, 'Toyota Prius', 'false')")
conn.commit()
conn.close()
'''

class QueryTemplate:
  def connect(self):
    self.conn = sqlite3.connect("sales.db")
  
  def construct_query(self):
    raise NotImplementedError()

  def do_query(self):
    results = self.conn.execute(self.query)
    self.results = results.fetchall()

  def format_results(self):
    output = []
    for row in self.results:
        row = [str(i) for i in row]
        output.append(", ".join(row))
    self.formatted_results = "\n".join(output)

  def output_results(self):
    raise NotImplementedError()

  # Template method
  def process_format(self):
    self.connect()
    self.construct_query()
    self.do_query()
    self.format_results()
    self.output_results()


class newVehiclesQuery(QueryTemplate):
  def construct_query(self):
    self.query = "select * from Sales where new='true'"
  
  def output_results(self):
    print(self.formatted_results)
  

class UserGrossQuery(QueryTemplate):
  def construct_query(self):
    self.query = ("select salesperson, sum(amt) " +
      " from Sales group by salesperson")

  def output_results(self):
      filename = "gross_sales_{0}".format(
        datetime.now().strftime("%Y%m%d")
      )

      with open(filename, "w") as outfile:
          outfile.write(self.formatted_results)

vehicle = newVehiclesQuery()
vehicle.process_format()

##usergorss = UserGrossQuery()
##usergorss.process_format()

print("-"*30)

# ADAPTER PATTERN
# Is used to work connecting two preexisting object even if they are not compatibles.

from datetime import datetime


class AgeCalculator:
  def __init__(self, birthday):
    self.year, self.month, self.day = (int(x) for x in birthday.split("-"))

  def calculate_age(self, date):
    year, month, day = (int(x) for x in date.split('-'))
    age = year - self.year

    if (month, day) < (self.month,self.day):
      age -= 1
    
    return age

class DateAgeAdapter:
  def _str_date(self, date):
    return date.strftime('%Y-%m-%d')
  
  def __init__(self, birthday):
    birthday = self._str_date(birthday)
    self.calculator = AgeCalculator(birthday)

  def get_age(self, date):
    date = self._str_date(date)
    return self.calculator.calculate_age(date)

age_calculator = AgeCalculator("1984-09-24")
age_with_calculator = age_calculator.calculate_age("2020-11-16")

now = datetime.today()
birthday_date = datetime(1984, 9, 24)

date_adapter = DateAgeAdapter(birthday_date)
adapter_get_age = date_adapter.get_age(now)

print(adapter_get_age)
print("-"*30)

# FACADE PATTERN
# Facade is, in many ways, like adapter. The primary difference is that the facade
# is trying to abstract a simpler interface out of a complex system;
# the adapter is only trying to map one existing interface to another.


# PROXY PATTERN
# Provides a placeholder to get access to that object. So you instead the Object directly
# you call the Proxy to get CONTROL ACCESS to the object.

# This example it supposed to fix the performance in a APP. Is just theorical.

class BookParser:
  def __init__(self, book):
    self.book = book 

  def get_number_pages(self):
    return len(self.book)


class BookParserProxy:
  def __init__(self, book):
    self.book = book
    self.parser = None 

  def get_number_pages(self):
    if self.parser == None:
      self.parser = BookParser(self.book)
    
    return self.parser.get_number_pages()

book = "Provides a placeholder to get access to that object. So you instead the Object directly"
#book_parser = BookParser(book)
parser_proxy = BookParserProxy(book)

print(parser_proxy.get_number_pages())
print("-"*30)

'''
Abstract Class
An abstract class is a class that is declared abstract — it may or may not include abstract methods.
Abstract classes cannot be instantiated, but they can be subclassed.
An abstract class may have static fields and static methods.

Interface
An interface is just the declaration of methods of an object; it’s not the implementation.
In an interface, we define what kind of operation an object can perform.
These operations are defined by the classes that implement the interface. 
Interfaces form a contract between the class and the outside world, 
and this contract is enforced at build time by the compiler.

interface Vehicle {
  // Declaration
  void changeGear(int newValue)
}

class Car implements Vehicle {
  int gear = 0
  // Implementation
  void changeGear(int newValue) {
    gear =  newValue
  }
}

'''

# Bridge PATTERN
# Separates the specific (MediaResource) Classess from the independent one (LongTermView).
# The result is less classes to make.

class LongTermView:
  def __init__(self, resource):
    self.resource = resource

  def show(self):
    content = self.resource.get_snippet()
    image = self.resource.get_image()

    return '<h1>{}</h1> <img src="{}">'.format(content, image)

class ShortTermView:
  def __init__(self, resource):
    self.resource = resource

  def show(self):
    content = self.resource.get_snippet()

    return '<h1>{}</h1>'.format(content)

class MediaResource(ABC):
  @abstractmethod
  def get_snippet(self):
    pass

  @abstractmethod
  def get_image(self):
    pass

class ArtistResource(MediaResource):
  def __init__(self):
    self.name = 'The artist''s name'
    self.bio = 'The artist''s bio'
    self.content = 'The artist''s tons of content'
    self.image = 'The artist''s photo'

  def get_snippet(self):
    return self.name + self.bio + self.content

  def get_image(self):
    return self.image

class BookResource(MediaResource):
  def __init__(self):
    self.title = 'The album name'
    self.cover = 'The album cover'

  def get_snippet(self):
    return self.title

  def get_image(self):
    return self.cover


book_media = BookResource()
artist_media = ArtistResource()

book_long_term_view = LongTermView(book_media)
book_short_term_view = ShortTermView(book_media)

artist_long_term_view = LongTermView(artist_media)
artist_short_term_view = ShortTermView(artist_media)


print(book_long_term_view.show())
print(book_short_term_view.show())
print(artist_long_term_view.show())
print(artist_short_term_view.show())


# Factory PATTERN
# It takes charge to instance new object from the same family, in different ways and/or different subtypes.

'''
  Create factory Class -> Creator Class that creates a product a this products implements a specific product.
  The products created have to have a relationship between them.
  Example APP with dark and light theme, the factory makes sure to send correct group of buttons and labels (both
  have consequence relationship between them) instances for each theme.
'''


# Abstract Factory PATTERN
# Is a set of factory methods.

print("-"*30)


# COMPOSITE PATTERN
# Composes objects into tree structure to represent part or full high hierarchies. The clients threads objects or hierarchies objects in an uniform way.

class Component:
  def __init__(self, name):
    self.name = name

  def move(self, new_path):
    new_folder = get_path(new_path)
    del self.parent.childrem[self.name]
    new_folder.children[self.name] = self
    self.parent = new_folder

  def copy(self, new_path):
    copy_name = self.name + '-copy'
    new_folder = get_path(new_path)
    new_folder.children[copy_name] = self
    self.parent = new_folder

  def delete():
    del self.parent.children[self.name]

class Folder(Component):
  def __init__(self, name):
    super().__init__(name)
    self.children = {}

  def add_child(self, child):
    child.parent = self
    self.children[child.name] = child

class File(Component):
  def __init__(self, name, contents):
    super().__init__(name)
    self.contents = contents

root = Folder('')
def get_path(path):
  names = path.split('/')[1:]
  node = root
  for name in names:
    node = node.children[name]
  print(node)
  return node

folder1 = Folder('folder1')
folder2 = Folder('folder2')
root.add_child(folder1)
root.add_child(folder2)
file111 = File('file111', 'contents')
folder1.add_child(file111)
#file111.copy('/folder1')