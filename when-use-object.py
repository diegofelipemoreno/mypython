import math
from urllib.request import urlopen

square = [(1,1), (1,2), (2,2), (2,1)]

def distance(p1, p2):
    return math.square((p1[0] + p2[0]) ** 2 + (p1[1] - p2[1] ** 2))

def perimeter(polygon):
    perimeter = 0
    points = polygon + [polygon[0]]
    for i in range(len(polygon)):
        perimeter += distance(points[i], points[i + 1])
    return perimeter



class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name
    
    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name
    
    def _get_name(self):
        return self._name
    
    name = property(_get_name, _set_name)

c = Color("#000ff", "bright red")
#c._set_name("oso")
#print(c._name)

# -- Using properties to add behavior to class data --
class Silly:
    def _get_silly(self):
        print("You are getting silly")
        return self._silly

    def _set_silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value

    def _del_silly(self, value):
        print("Whoa, you killed silly!")
        del self._silly
    
    silly = property(_get_silly, _set_silly, _del_silly, "This is a silly property")


#s = Silly()
#s.silly = "Funny"
#s._set_silly("Bear")
#s._get_silly()
#print(s.silly)
#s._del_silly("Bear")
#print(help(s))


# --- Decorators: another way to create properties ---
class Silly:
    @property
    def silly(self):
        "This is a silly property"
        print("You are getting silly")
        return self._silly
    
    @silly.setter
    def silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value

    @silly.deleter
    def silly(self):
        print("Whoa, you killed silly!")
        del self._silly

#s = Silly()
#s.setter("Bear")
#print(s.value)

class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print("Retrieving New Page...")
            self.__content = urlopen(self.url).read()
        return self._content

#import time
#webpage = WebPage("http://ccphillips.net/")
#now = time.time()
#content1 = webpage.content
#print(time.time())

class AverageList(list):
    @property
    def average(self):
        return sum(self) / len(self)

a = AverageList([1, 2, 3, 4])
print(a.average)



# -- Managing objects --

import sys
import os
import shutil
import zipfile

class ZipReplace:
    def __init__(self, filename, search, search_string, replace_string):
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = "unzipped-{}".format(filename)

    def _full_filename(self, filename):
        return os.path.join(self.temp_directory, filename)

    def zip_find_replace(self):
        self.unzip_files()
        self.find_replace()
        self.zip_files()
    
    def unzip_files(self):
        os.mkdir(self.temp_directory)
        zip = zipfile.ZipFile(self.filename)
        try: 
            zip.extractall(self.temp_directory)
        finally:
            zip.close()

    def find_replace(self):
        for filename in os.listdir(self.temp_directory):
            with open(self._full_filename(filename)) as file:
                contents = file.read()
            contents = contents.replace(
                self.search_string, self.replace_string)
            with open(self._full_filename(filename), "w") as file:
                file.write(contents)
    
    def zip_files(self):
        file = zipfile.ZipFile(self.filename, "w")
        for filename in os.listdir(self.temp_directory):
            file.write(self._full_filename(filename), filename)
        shutil.rmtree(self.temp_directory)

if __name__ == "__main__":
    ZipReplace(*sys.argv[1:4]).zip_find_rep

