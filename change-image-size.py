from pygame import image
from pygame.transform import scale
import os
import sys

class ChangeImgSize:
    def __init__(self, file_path):
        self.file_path = file_path
        self.img_list = []

    def resize_image(self):
      img = image.load(self.file_path)
      filename = os.path.splitext(self.file_path)[0]
      file_ext = os.path.splitext(self.file_path)[1]
      scaled = scale(img, (640, 480))
      image.save(scaled, filename + '-640' + file_ext)

      print(image)
        
    def process(self):
      self.resize_image();

if __name__ == '__main__':
    for arg in sys.argv[1:]:
      ChangeImgSize(arg).process()
