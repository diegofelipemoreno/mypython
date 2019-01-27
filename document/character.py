
import sys
from cursor import Cursor

class Character:
    def __init__(self, character, bold=False, italic=False, underline=False):
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __string__(self):
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else ''

        return bold + italic + underline + self.character