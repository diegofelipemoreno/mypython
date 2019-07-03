import os
import pdb
import sys
import shutil

class FindeImgsOnFolders:

    def __init__(self, folder_path):
        self.folder_path = folder_path
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
        folder_output_path = self.folder_path[:index_folder_output]
        name_folder_output = "all-imgs"
        path_folder_output = folder_output_path + "/" + name_folder_output

        try:
            os.mkdir(path_folder_output)
        except OSError:
            print("Folder {} already exist".format(name_folder_output))

        for imgs in self.dict_imgs.items():
            for img in imgs[1]:
                dst = img.split(".")[0] + "__" + str(imgs[0]) + "." + img.split(".")[1]
                salida = os.rename(img, dst) 
                #shutil.copy(salida, path_folder_output)
                print(dst)

    def init(self):
        """
        Initialize.
        """
        self.save_files()
        #print(self.folder_path)


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        FindeImgsOnFolders(arg).init()