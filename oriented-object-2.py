import pdb
import shutil
import os
import datetime
import time

def hello(*arg):
    if not len(arg):
        arg = []
    arg.append('a')
    print(arg)

#hello()

def get_pages(*links):
    for link in links:
        print(link)

#get_pages('http://www.archlinux.org')

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
#print(options.__getitem__('username'))


# ----------------------Variable argument lists-------------------------
def augmented_move(target_folder, *filenames, verbose=False, **specific):
    '''Move all filenames into the target_folder,
     allowing specific treatment of certainr files.'''

    def print_verbose(message, filename):
        ''' Print message only if verbose is enabled'''
        if verbose:
            print(message.format(filename))

    def are_assets_exists():
        ''' Checks if folder and files exist'''

        exists_file = os.path.exists(filename)
        exists_folder = os.path.exists(target_folder)

        if not exists_file and not exists_folder:
            raise FileNotFoundError([filename, target_folder])
        elif exists_file and not exists_folder:
            raise FileNotFoundError(target_folder)
        elif exists_folder and not exists_file:
            raise FileNotFoundError(filename)

    for filename in filenames:
        target_path = os.path.join(target_folder, filename)

        try:
            are_assets_exists()
        except FileNotFoundError as error_files: 
            print("Error, {} missing.".format(error_files))
        else:
            if filename in specific['specific']:
                if specific['specific'][filename] == 'ignore':
                    print_verbose("Ignoring {0}", filename)
                elif specific['specific'][filename] == 'copy':
                    print_verbose("Copying {0}", filename)
                    shutil.copyfile(filename, target_path)
            else:
                print_verbose("Moving {0}", filename)
                shutil.move(filename, target_path)

# augmented_move("folder_to_move_files", "mypython.py", "database.py",  verbose=True, specific={"mypython.py": "copy"})


# ----------------------Unpacking arguments-------------------------
def show_args(arg1, arg2, arg3="THREE"):
    print(arg1, arg2, arg3)

some_args = ['a', 'b', 'c']
more_args = {
 "arg1": "ONE",
 "arg2": "TWO"
}

print("Unpacking a sequence:", end=" ")
show_args(*some_args)

print("Unpacking a dict:", end=" ")
show_args(**more_args)


# ----------------------Functions are objects too-------------------------
print("-"*30)

def my_function():
    print("The Function was called")

my_function.description = "A silly function."


def second_function():
    print("The second was called")
second_function.description = "A sillier function."


def another_function(function):
    print("The description:", end=" ")
    print(function.description)
    print("The name:", end=" ")
    print(function.__name__)
    print("The class:", end=" ")
    print(function.__class__)
    print("Now I'll call the function passed in")
    function()

another_function(my_function)
another_function(second_function)

print("xxxxx")
my_function()
second_function()

print("-"*30)

class TimedEvent:
    def __init__(self, endtime, callback):
        self.endtime = endtime
        self.callback = callback

    def ready(self):
        return self.endtime <= datetime.datetime.now()

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


#timer = Timer()
#timer.call_after(1, one)
#timer.call_after(2, three)
#timer.call_after(5, two)
#timer.run()

print("-"*30)

# ----------------------Using functions as attributes-------------------------
class A:
    def print(self):
        print("my class is A")

def fake_print():
    print("my class is not A")

a = A()
a.print()
a.print = fake_print
a.print()

# ----------------------Callable objects-----------------------
print("-"*30)

class Repeater:
    def __init__(self):
        self.count = 0
    def __call__(self, timer):
        format_time("{now}: repeat {0}", self.count)
        self.count += 1
        timer.call_after(5, self)

timer = Timer()
timer.call_after(5, Repeater())
format_time("{now}: Starting")
#timer.run()