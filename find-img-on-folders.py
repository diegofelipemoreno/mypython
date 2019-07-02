import os
import re
import sys

EXT_IMG_REGEX = "/.\png|.\jpg|.\gif/gm"

class FindImgsOnFolder:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self._tempfolders = self.tempfolders
        self._temp_img_files = self.temp_img_files

    @property
    def temp_img_files(self):
        dict_img = {}
        current_folder_path = self.folder_path

        def _save_on_dict_img(file_list):
            for file in file_list:
                if ".jpg" in file or ".png" in file or ".gif" in file:
                    print(current_folder_path + "/" + file)


        # r=root, d=directories, f = files
        for directories in os.walk(self.folder_path):
            for current_file in directories:
                if current_file and type(current_file) is list:
                    _save_on_dict_img(current_file)
                else: 
                    pass

    @property
    def tempfolders(self):
        folders = []

        # r=root, d=directories, f = files
        for r, d, f in os.walk(self.folder_path):
            for folder in d:
                folders.append(os.path.join(r, folder))

        return folders

    def _matches(self, regexp, segment):
        """Matches segment with regexp provided.

        Args:
           String: regexp Pattern to match.
           String: segment To be macthed.

        Returns:
            True if it matches, False if not.
        """
        return bool(re.match(re.compile(regexp), segment))

    def init(self):
        """
        Initialize.
        """
        pass

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        FindImgsOnFolder(arg).init()