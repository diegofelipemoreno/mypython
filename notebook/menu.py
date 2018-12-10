class Note:
    'Represents a message from the notebook'

    def __init__(self, tag='', date=''):
        '''Initialize  a new message for the notebook'''
        self.tag = tag
        self.date = date

    def reset(self):
        self.x = 0
        self.y = 0

myNote = Note('thong', 'now')
print(myNote.tag, myNote.date)