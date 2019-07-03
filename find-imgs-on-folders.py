import os
import pdb
import sys
import shutil
from shutil import copyfile

class FindeImgsOnFolders:
    def __init__(self, folder_path, destiny_path=""):
        self.folder_path = folder_path
        self.destiny_path = destiny_path
        self._dict_imgs = self.dict_imgs

    @property
    def dict_imgs(self):
        """
        Gets dict imgs.

        Return:
        Dict images.
        """

        dict_img_filtered = {}

        for root, directories, files in os.walk(self.folder_path):

            for file in files:
                if ".jpg" in file or ".jpeg" in file or ".png" in file or ".gif" in file or ".svg" in file:
                    has_name_file = abs(hash(root + "/" + file))
                    full_path_file = root + "/" + file
                    
                    if  not dict_img_filtered.get(has_name_file):
                        dict_img_filtered[has_name_file] = []
                                        
                    dict_img_filtered[has_name_file].append(full_path_file)

        return dict_img_filtered

    def save_files(self):
        """
        Creates a folder and save all the imgs on it.
        """

        index_folder_output = self.folder_path.rfind("/")
        folder_output_path = self.destiny_path or self.folder_path[:index_folder_output]
        name_folder_output = "all-imgs"
        path_folder_output = folder_output_path + "/" + name_folder_output
       
        try:
            os.mkdir(path_folder_output)
        except OSError:
            print("Folder {} already exist".format(name_folder_output))
        finally:
            for imgs in self.dict_imgs.items():
                for img in imgs[1]:
                    path, filename = os.path.split(img)
                    filename_renamed = filename.split(".")[0] + "__" + str(imgs[0]) + "." + img.split(".")[1]
                    path_destiny_img = path_folder_output + "/" + filename_renamed
                    copyfile(img, path_destiny_img) 

    def init(self):
        """
        Initialize.
        """
        self.save_files()

if __name__ == "__main__":
    FindeImgsOnFolders(*sys.argv[1:3]).init() 