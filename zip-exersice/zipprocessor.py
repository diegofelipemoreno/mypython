# -- Managing objects composition --
import sys
from pygame import image
from pygame.transform import scale
import os
import shutil
import zipfile
import pdb

#pdb.set_trace()

class ZipProcessor:
    def __init__(self, processor):
        self._ext_file = 'zip'
        self._zipfile_list = self.zipfile_list
        self._zipfile_tempfolder = self.zipfile_tempfolder
        self._tempfolder = self.tempfolder
        self.processor = processor

    @property
    def tempfolder(self):
        temp_folder_list = []

        for file in self.zipfile_list:
            temp_folder_list.append("unzipped-{}".format(file.split('.')[0]))
    
        return temp_folder_list

    @property
    def zipfile_list(self):
        file_list = []

        for file in os.listdir("./"):
            if file.endswith(".{}".format(self._ext_file)):
                file_list.append(file)

        return file_list

    @property
    def zipfile_tempfolder(self):
        return zip(self.zipfile_list, self.tempfolder)

    def path_files_zip(self, file, current_folder):
        return os.path.join(current_folder, file)

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

    def zip_files(self):
       
        def _get_files(tem_folder):
            return os.listdir(tem_folder)
        
        def _set_files_zip(files_list, zip_file_name, temp_folder):
            file_zip = zipfile.ZipFile(zip_file_name, "w")

            for file in files_list:
                file_zip.write(self.path_files_zip(file, temp_folder), file)
            shutil.rmtree(temp_folder)
            
        for file_tuple in self.zipfile_tempfolder:
            zip_file_name = file_tuple[0]
            temp_folder = file_tuple[1]
            files = _get_files(temp_folder)
            _set_files_zip(files, zip_file_name, temp_folder)
            

    def process_zip(self):
        self.unzip_zipfile()
        self.processor.process(self)
        self.zip_files()


class ZipReplace():
    def __init__(self, search_string, replace_string):
        self.replace_string = replace_string
        self.search_string = search_string

    def process(self, zipprocessor):
        '''perform a search and replace on all files
            in the temporary directory'''

        def _replace_string(full_path_file):
            with open(full_path_file) as current_file:
                contents = current_file.read()
                contents = contents.replace(
                    self.search_string, self.replace_string)
            
            with open(full_path_file, "w") as file:
                file.write(contents)

        for folder in zipprocessor.tempfolder:
            current_folder = folder

            for file in os.listdir(folder):
                full_path_file = zipprocessor.path_files_zip(file, current_folder)

                if full_path_file:
                    try:
                        _replace_string(full_path_file)
                    except IsADirectoryError as exception:
                        print(exception)
                    except UnicodeDecodeError as exception:
                         print("{}. File: {}".format(exception, full_path_file))
                    except FileNotFoundError as exception:
                         print(exception)
                    else:
                        _replace_string(full_path_file)
        

class ScaleZip():

    def process(self, zipprocessor):
        '''Scale each image in the directory to 640x480'''

        for folder in zipprocessor.tempfolder:
            current_folder = folder

            for file in os.listdir(folder):
                full_path_file = zipprocessor.path_files_zip(file, current_folder)

                if full_path_file:
                    try:
                        im = image.load(full_path_file)
                    except Exception as exception:
                        print("File: {}. {}".format(file, exception))
                    else:
                        im = image.load(full_path_file)
                        scaled = scale(im, (640,480))
                        image.save(scaled, full_path_file)


if __name__ == "__main__":
    #print(ZipProcessor(zipreplace).__dict__)
    zipreplace = ZipReplace(*sys.argv[1:3])
    ZipProcessor(zipreplace).process_zip()

    #print(ZipProcessor(ScaleZip).__dict__)
    scaleZip = ScaleZip()
    ZipProcessor(scaleZip).process_zip()

    
