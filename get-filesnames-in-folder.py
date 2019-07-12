import os
import pdb
import sys

class GetFilenamesInFolder:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self._filename_set = self.filename_set

    @property
    def filename_set(self):
        current_filename_set = set()
    
        for root, dirs, files in os.walk(self.folder_path):
            for file in files:
                path, filename = os.path.split(file)
                filename_filtered = "/" + filename.split("__")[0] + "\." + filename.split(".")[1] + "/"
                current_filename_set.add(filename_filtered)
                #current_filename_set.add(filename)

        return sorted(current_filename_set)

    def output_result(self):
        """ Outputs results on a txt file.

        Returns:
            Txt file.
        """
        outname = "./assets/filenames-imgs-all.txt"

        with open(outname, "w") as outfile:
                for filename_text in self.filename_set:
                    outfile.write(filename_text + ",\r\n")

    def init(self):
        """
        Initialize.
        """
        self.output_result()
        #print(self.filename_set)
                    

if __name__ == "__main__":
    GetFilenamesInFolder(sys.argv[1]).init() 
