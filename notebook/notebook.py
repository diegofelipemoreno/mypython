import datetime
import pdb

# Store the next available id for all new notes
last_id = 0

class Note:
    '''Represent a note in the notebook. Match against a
       string in searches and store tags for each note.'''

    def __init__(self, memo='', tags=''):
        '''initialize a note with memo and optional
           space-separated tags. Automatically set the note's
           creation date and a unique id.'''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''Determine if this note matches the filter
           text. Return True if it matches, False otherwise.
           Search is case sensitive and matches both text and tags.'''
        return filter in self.memo or filter in self.tags

    def match_by_id(self, filter):
        return filter in self.id

class Notebook:
    '''Represent a collection of notes that can be tagged,
       modified, and searched.'''

    def __init__(self):
        '''Initialize a notebook with an empty list.'''
        self.notes = []

    def new_note(self, memo=''):
        '''Create a new note and add it to the list.'''
        if memo == '':
            self.notes.append(Note())
        else:
            self.notes.append(Note(memo))
    
    def modify_memo(self, note_id, memoText):
        '''Find the note with the given id and change its
        memo to the given value.'''
        self._find_note(note_id).memo = memoText

    def modify_tags(self, note_id, tags_text):
        '''Find the note with the given id and change its
        tags to the given value.'''
        self._find_note(note_id).tags = tags_text
    
    def _find_note(self, note_id):
        '''Find the note from id'''
        for note in self.notes:
            if note.id == note_id:
               return note
        return None

    def show_notes(self):
        '''list all notes'''
        return self.notes

    def search(self, filterText):
        '''Find the note from text'''
        return [note for note in self.notes if
                note.match(filterText)]

    def search_by_id(self, id):
        '''Find the note from id'''
        return [note for note in self.notes if
                note.match_by_id(id)]



#n1 = Note('first note')
#n2 = Note('second note')
#mynotebook = Notebook()
#mynotebook.new_note(n1)
#mynotebook.new_note(n2)
#mynotebook.modify_memo(2, 'second changed note')
#mynotebook.modify_tags(1, 'im tags form 1')

#print(mynotebook._find_note(2).__dict__)
