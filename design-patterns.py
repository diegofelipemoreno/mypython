import pdb
import time
import datetime
import smtplib
import imaplib


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

#from pygame import image
#from pygame.transform import scale
#from pygame import Surface

class TileStrategy:
    def make_background(self, img_file, desktop_size):
        in_img = image.load(img_file)
        out_img = Surface(desktop_size)
        
        for x in range((out_img.get_width() // in_img.get_width()) + 1):
            for y in range((out_img.get_height() // in_img.get_height()) + 1):
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

class Node:
    def __init__(self, tag_name, parent=None):
        self.parent = parent
        self.tag_name = tag_name
        self.children = []
        self.text = ""

    def __str__(self):
        if self.text:
            return self.tag_name + ": " + self.text
        else:
            return self.tag_name

class FirstTag:
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find("\n")
        i_end_tag = remaining_string.find("\n")
        tag_name = remaining_string[i_start_tag+1:i_end_tag]
        root = Node(tag_name)
        parser.root = parser.current_node = root
        parser.state = ChildNode()
        return remaining_string[i_end_tag+1:]

class ChildNode:
    def process(self, remaining_string, parser):
        stripped = remaining_string.strip()
        if stripped.startswith("</"):
            parser.state = CloseTag()
        elif stripped.startswith("<"):
            parser.state = OpenTag()
        else:
            parser.state = TextNode()
        return stripped

class OpenTag:
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find("<")
        i_end_tag = remaining_string.find(">")
        tag_name = remaining_string[i_start_tag+1:i_end_tag]
        node = Node(tag_name, parser.current_node)
        parser.current_node.children.append(node)
        parser.current_node = node
        parser.state = ChildNode()
        return remaining_string[i_end_tag+1:]

class CloseTag:
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find('<')
        i_end_tag = remaining_string.find('>')
        assert remaining_string[i_start_tag+1] == "/"
        tag_name = remaining_string[i_start_tag+2:i_end_tag]

        if parser.current_node.tag_name:
            assert tag_name == parser.current_node.tag_name
            parser.current_node = parser.current_node.parent
            parser.state = ChildNode()
            return remaining_string[i_end_tag+1:].strip()

class TextNode:
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find("<")
        text =  remaining_string[:i_start_tag]
        parser.current_node.text = text
        parser.state = ChildNode()
        return remaining_string[i_start_tag:]

if __name__ == "__main__":
    import sys
    '''
    with open(sys.argv[1]) as file:
        contents = file.read()
        p = Parser(contents)
        p.start()

        nodes = [p.root]
        while nodes:
            node = nodes.pop(0)
            print(node)
            nodes = node.children + nodes 
    '''

''' State versus strategy 
The strategy pattern is used to choose an algorithm at runtime; generally, only one of
those algorithms is going to be chosen for a particular use case. The state pattern, on
the other hand is designed to allow switching between different states dynamically,
as some process evolves. In code, the primary difference is that the strategy pattern
is not typically aware of other strategy objects. In the state pattern, either the state or
the context needs to know which other states that it can switch to.
'''


# --------- Singleton pattern --------------
'''
__new__ class method to ensure that only one instance
is ever created
'''

class OneOnly:
    _singleton = None
    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(OneOnly, cls).__new__(cls, *args, **kwargs)
        return cls._singleton


# --------- Template pattern --------------

import sqlite3

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
    
    def process_format(self):
        self.connect()
        self.construct_query()
        self.do_query()
        self.format_results()
        self.output_results()


class NewVehiclesQuery(QueryTemplate):
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
            datetime.date.today().strftime("%Y%m%d")
        )

        with open(filename, "w") as outfile:
            outfile.write(self.formatted_results)

vehicle = NewVehiclesQuery()
vehicle.process_format()

#usergorss = UserGrossQuery()
#usergorss.process_format()

print("-"*30)


# --------- Adapter pattern --------------
'''
Adapters are used to allow two preexisting objects to work together,
even if their interfaces are not compatible.
'''

class AgeCalculator:
    def __init__(self, birthday):
        self.year, self.month, self.day = (
            int(x) for x in birthday.split('-'))
    
    def calculate_age(self, date):
        year, month, day = (
            int(x) for x in date.split('-')) 
        now = datetime.datetime.now()
        age_year = now.year - year - 1 
        age_month = month - now.month
        age_day = now.day - day
        print("{0} Years, {1} months, {2} days".format(age_year, age_month, age_day))

class DateAgeAdapter:
    def _str_date(self, date):
        return date.strftime("%Y-%m-%d")

    def __init__(self, birthday):
        birthday = self._str_date(birthday)
        self.calculator = AgeCalculator(birthday)

    def get_age(self, date):
        date = self._str_date(date)
        return self.calculator.calculate_age(date)


mydate = datetime.datetime(1984, 9, 24)
dateAgeAdapter = DateAgeAdapter(mydate)
dateAgeAdapter.get_age(mydate)

print("-"*30)

# --------- Facade pattern --------------
'''
--Email Exercise a way to do a simple task send and receive an email--
The facade pattern is designed to provide a simple interface to a complex system
of components. The objects in this system may need to be interacted with directly
for complex tasks and interactions. Often, however, there is 'typical' usage for the
system, and these complicated interactions aren't necessary in that common scenario. 
'''

class EmailFacade:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, message):
        ''' 
            Sends Email with subject, message

            Args:
            String: valid email.
            String: subject.
            String: message.
        '''

        if not "@" in username:
            from_email = "{0}@{1}".format(self.username, self.host)
        else:
            from_email = self.username
        
        message = ("From: {0}\r\n"
                   "To: {1}\r\n"
                   "Subject: {2}\r\n\r\n{3}").format(
                       from_email, to_email, subject, message)

        smtp = smtplib.SMTP(self.host)
        smtp.login(self.username, self.password)
        smtp.sendmail(from_email, [to_email], message)

    def get_inbox(self):
        mailbox = imaplib.IMAP4(self.host)
        mailbox.login(bytes(self.username, "utf8"), 
                      bytes(self.password, "utf8"))
        mailbox.select()
        x, data = mailbox.search(None, 'All')
        messages = []
        for num in data[0].split():
            x, message = mailbox.fetch(num, "(RFC822)")
            messages.append(message[0][1])
        return messages

print("-"*30)

# --------- Abstract factory pattern --------------

