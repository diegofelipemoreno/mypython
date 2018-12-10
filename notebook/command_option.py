import sys
from notebook import Notebook, Note

class Menu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_all_notes,
            "2": self.search_notes,
            "3": self.add_notes,
            "4": self.modify_notes
            }
        self.modifyChoices = {
            "1": self.modify_note_tag,
            "2": self.modify_note_memo
            }

    def display_menu(self):
        print("""
    Notebook Menu
    1. Show all Notes
    2. Search Notes
    3. Add Note
    4. Modify Note
    5. Quit
""")

    def display_modify_note(self):
        print("""
    Enter what do you want to modify
    1. Tag
    2. Memo
""")

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action: 
                action()
            else:
                print("{0} is not a valid choice".format(choice))
        
    def show_all_notes(self, notes=[]):
        #import ipdb; ipdb.set_trace()
        if len(self.notebook.notes) == 0:
            notes = self.notebook.notes
            print(notes)
            print(len(notes))
        else:
            for note in self.notebook.notes:
                print("mostro otras")
                print(note.__dict__)
                print("{0}: {1} {2} {3}".format(
                note.id, note.tags, note.memo, note.creation_date))

    def search_notes(self):
        textToLook = input("Search for ")
        found = self.notebook.search(textToLook)
        if len(found) == 0:
            print("{0}: element is not on the notebook".format(textToLook))
        else:
            for note in found:
                print("{0}: {1} {2} {3}".format(
                note.id, note.tags, note.memo, note.creation_date))

    def search_notes_for_id():
        textToLook = input("Select the note id to modify ")
        found = self.notebook.search_by_id(textToLook)
        foundNote = {}
        if len(found) == 0:
            print("{0}: element is not on the notebook".format(textToLook))
        else:
            print(note, '----->')
            
    def add_notes(self):
        memo = input("Enter a memo: ")
        new_note = self.notebook.new_note(memo)
    
    def modify_notes(self):
        self.show_all_notes()
        self.search_notes_for_id()
        '''
        self.display_modify_note()
        toModify = input("Enter what do you want to modify: ")
        action = self.modifyChoices.get(toModify)
        if action: 
            action()
        else:
            print("{0} is not a valid choice".format(toModify))
        '''

    def modify_note_memo(self, noteId):
        print('---->', self.notebook.id)

    def modify_note_tag(self, noteId):
        print('---->', self.notebook.id)
            
    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
