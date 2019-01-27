
import sys
from cursor import Cursor
from character import Character

class Document:
    def __init__(self):
        self.characters = []
        self.filename = ''
        self.cursor = Cursor(self)
        self._string = self.string

    @property
    def string(self):
        output = ""
        #output = "".join((str(c) for c in self.characters))
        for character in self.characters:
            output += character.__string__()
        print(output)
        return output

    def insert(self, character):
        if not hasattr(character, 'character'):
               character = Character(character)
        self.characters.append(character)
        self.cursor.position += 1

    def delete(self):
        del self.characters[self.cursor.position]
    
    def save(self):
        f = open(self.filename, 'w')
        f.write(''.join(self.characters))
        f.close()
    
    def forward(self):
        self.cursor.position +=1

    def back(self):
        self.cursor.position -=1

d = Document()
d.insert('h')
d.insert('e')
d.insert(Character('l', bold=True))
d.insert(Character('l', bold=True))
#print(d.cursor.position)
d.insert('o')
d.insert('\n')
d.insert(Character('w', italic=True))
d.insert(Character('o', italic=True))
d.insert(Character('r', underline=True))
#print(d.cursor.position)
d.insert('l')
d.insert('d')
d.insert("*")
#print(d.cursor.position)
#d.cursor.home()
d.string
#d.cursor.home()
#print(d.__dict__)
#print(d.cursor.__dict__)
