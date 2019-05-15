import pdb
import time


# ------ Decorator Pattern -----------

def log_calls(func):
    def wrapper(*args, **kwargs):
        now = time.time()
        print("Calling {0} with {1} and {2}".format (
            func.__name__, args, kwargs))
        return_value = func(*args, **kwargs)
        print("Executed {0} in {1}ms".format(
            func.__name__, time.time() - now))
        return return_value
    return wrapper

# '@log_calls' Syntax in order to use apply the decorator directly and avoid 
# the basic approach Ex: test2, test3
@log_calls 
def test1(a, b, c):
    print("\ttest1 called")

def test2(a, b):
    print("\ttest 2 called")

def test3(a, b):
    print("\ttest 3 called")
    time.sleep(2)

'''
test2 = log_calls(test2)
test3 = log_calls(test3)

test1(1,2,3)
test2(4,b=5)
test3(6,7)
'''


print("-"*30)
# ------ Observer Pattern -----------

class Inventory:
    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0
    
    def attach(self, observer):
        self.observers.append(observer)

    @property
    def product(self):
        return self._product
    @product.setter
    def product(self, value):
        self._product = value
        self._update_observers()

        return self._product

    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self._update_observers()

    def _update_observers(self):
        for observer in self.observers:
            observer()

class ConsoleObserver:
    def __init__(self, inventory):
        self.inventory = inventory

    def __call__(self):
        print(self.inventory.product)
        print(self.inventory.quantity)

i = Inventory()
c = ConsoleObserver(i)
i.attach(c)
i.product = "Widget"
i.quantity = 5


print("-"*30)
# ------ Strategy pattern -----------

from pygame import image
from pygame.transform import scale
from pygame import Surface

class TileStrategy:
    def make_background(self, img_file, desktop_size):
        in_img = image.load(img_file)
        out_img = Surface(desktop_size)
        
        for x in range((out_img.get_width() // in_img.get_width()) + 1):
        for y in range((out_img.get_height( // in_img.get_height()) + 1):
        out_img.blit(in_img, (in_img.get_width() * x,
        in_img.get_height() * y))

        return out_img

class CenteredStrategy:
    def make_background(self, img_file, desktop_size):
        in_img = image.load(img_file)
        out_img = Surface(desktop_size)
        out_img.fill((0,0,0))
        
        left = (out_img.get_width() - in_img.get_width()) / 2
        top = (out_img.get_height() - in_img.get_height()) / 2
        out_img.blit(in_img, (left, top))
        
        return out_img

class ScaledStrategy:
    def make_background(self, img_file, desktop_size):
        in_img = image.load(img_file)

        return scale(in_img, desktop_size)

# --------- State pattern --------------

class Parser:
    def __init__(self, parse_string):
        self.parse_string = parse_string
        self.root = None
        self.current_node = None
        self.state = FirstTag()

    def process(self, remaining_string):
        remaining = self.state.process(remaining_string, self)
        if remaining:
            self.process(remaining)

    def start(self):
        self.process(self.parse_string)