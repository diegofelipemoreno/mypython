# -- Managing objects --

import sys
import os
import shutil
import zipfile
import pdb

#pdb.set_trace()

class ZipReplace:
    def __init__(self, search_string, replace_string):
        self._ext_file = 'zip'
        self._zipfile = self.zipfile
        self._zipfile_tempfolder = self.zipfile_tempfolder
        self._tempfolder = self.tempfolder
        self.replace_string = replace_string
        self.search_string = search_string

    @property
    def tempfolder(self):
        temp_folder_list = []
        for file in self._zipfile:
            temp_folder_list.append("unzipped-{}".format(file.split('.')[0]))
    
        return temp_folder_list

    @property
    def zipfile(self):
        #print(os.listdir("./"))
        file_list = []
        for file in os.listdir("./"):
            if file.endswith(".{}".format(self._ext_file)):
                file_list.append(file)

        return file_list

    @property
    def zipfile_tempfolder(self):
        return zip(self.zipfile, self.tempfolder)
    
    def _path_zipfile(self, zipfile):
        zipfile_name = zipfile.split('.')[0]
        
        for temp_folder in self.tempfolder:
            if zipfile_name and zipfile_name in temp_folder:
                return os.path.join(temp_folder, zipfile)
    
    def unzip_zipfile(self):
        for file_tuple in self.zipfile_tempfolder:
            zip_file_name = file_tuple[0]
            temp_folder = file_tuple[1]

            try:
                os.mkdir(temp_folder)
            except OSError:
                print("Folder {} already exist".format(temp_folder))

            zip = zipfile.ZipFile(zip_file_name)

            try: 
                zip.extractall(temp_folder)
            finally:
                zip.close()

    def find_replace(self):
        for folder in self.tempfolder:
            for file in os.listdir(folder):
                full_path_file = self._path_zipfile(file)

                if full_path_file:
                    with open(full_path_file) as file:
                        contents = file.read()
                    contents = contents.replace(
                        self.search_string, self.replace_string)

                    with open(full_path_file, "w") as file:
                        file.write(contents)
    
    def zip_files(self):

        def _get_file(tem_folder):
            return os.listdir(tem_folder)[0]
                
        for file_tuple in self.zipfile_tempfolder:
            zip_file_name = file_tuple[0]
            temp_folder = file_tuple[1]
            file = _get_file(temp_folder)
            file_zip = zipfile.ZipFile(zip_file_name, "w")
            file_zip.write(self._path_zipfile(file), file)
            shutil.rmtree(temp_folder)
    
    def zip_find_replace(self):
        self.unzip_zipfile()
        self.find_replace()
        self.zip_files()

if __name__ == "__main__":
    ZipReplace(*sys.argv[1:3]).zip_find_replace()

