import pdb
import sys
import os
import re

REGEXP_TODO = ".TODO\(|.TODO \(|@TODO"
REGEXP_VALID_FILES = '.*\.scss|.*\.tpl|.*\.html|.*\.py|.*\.yaml|.*\.js|.*\.md'
REGEXP_IS_A_FILE = '.*\..*'
INVALID_FOLDERS = ['dist', 'node_modules', 'static', 'lib', 'anaconda3', 'python3.6']

class GetToDos:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.todo_list = []
        self._list_files = self.list_files
        self._list_lines = self.list_lines

    @property
    def list_files(self):
        """
        Gets list of files.

        Return:
        List of folder's list
        """

        files_list = []
        for root, directories, files in os.walk(self.folder_path):
            flag = False

            for file in files:
                is_valid_type_file = re.match(REGEXP_VALID_FILES, file)
                is_valid_file = re.match(REGEXP_IS_A_FILE, file)
                
                if is_valid_type_file and is_valid_file and file not in INVALID_FOLDERS:
                    files_list.append(root + '/' + file)

        return files_list

    @property
    def list_lines(self):
        """
        Gets list of all the file lines.
        """
        line_list = []
        for file in self.list_files:
            with open(file, 'rb') as current_file:
                line = current_file.readline()
                line_list.append(line)

        return line_list

    def get_todos(self):
        """
        Gets list of all the file lines.
        """
        line_todo_list = []
        for line in self.list_lines:
            print(line)

        return line_todo_list

    def _matches(self, regexp, segment):
        """Matches segment with regexp provided.

        Args:
           String: regexp Pattern to match.
           String: segment To be macthed.

        Returns:
        Boolean True/False.
        """
        pattern_regexp = re.compile(regexp)

        return re.match(pattern_regexp, segment)

    def run(self):
        print(self.get_todos())

if __name__ == "__main__":
    GetToDos(*sys.argv[1:2]).run() 
        
        