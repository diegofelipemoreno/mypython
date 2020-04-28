# This Python file uses the following encoding: utf-8

import os
import pdb
import re
import sys
import json 

FOLDER_PATH = '/Users/diegofelipemoreno/Downloads/CARTAS/filter/'
NO_BREAK_SPACE_CHAR = '^\d{1,}.-{1,}|\d\-{1,}'
cards_Model_dict = {
           'id': '',
           'name': '',
           'img': ''
         }

class ProcessImageToJson:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.img_list = []

    def write_image_data_json(self):
      json_dict = {'cardsModel': self.img_list}
      json_object = json.dumps(json_dict, indent = 4) 

      with open('oso.json', 'w') as outfile: 
        outfile.write(json_object) 

    def rename_image_name(self):
        for file in os.listdir(self.folder_path):
          word_on_regex = re.findall(NO_BREAK_SPACE_CHAR, file)

          if word_on_regex:
            image_name = file.replace(word_on_regex[0], '')
            image_name_filtered = image_name.replace('-',' ').replace('.jpg', '').lower()
            #mage_name_filtered = image_name_filtered.encode('utf8')
            new_name_file = image_name.decode('ascii', errors='ignore').encode('ascii')
            new_name_file = new_name_file.lower()
            image_id = new_name_file.replace('.jpg', '')
            newfile_path = '{}{}'.format(FOLDER_PATH, new_name_file)
            file_path = '{}{}'.format(FOLDER_PATH, file)
            image_dict = {
                'id': image_id,
                'name': str(image_name_filtered),
                'img': newfile_path
              }

            self.img_list.append(image_dict)
            os.rename(file_path, newfile_path)
        
    def process(self):
      self.rename_image_name();
      #self.write_image_data_json();

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        ProcessImageToJson(arg).process()