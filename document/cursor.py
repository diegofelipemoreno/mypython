import pdb

#pdb.set_trace()

class Cursor:
    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        self.position += 1

    def back(self):
        self.position -= 1

    def home(self):
        try:
            docCharacterPos = self.document.characters[self.position - 1].character
            #print(docCharacterPos, self.position)
            while self.position > 0 and docCharacterPos != '\n':
                self.position -= 1
        finally:
            return

    def end(self):
        try:
            docCharacterPos = self.document.characters[self.position + 1].character
            docCharactersLength = len(self.document.characters)

            while self.position < docCharactersLength:
                self.position += 1
        finally:
            return