# coding: UTF-8
from config import *
from glob import glob

class ParserFile:

  def __init__(self):
    self.all_files = glob(PATH_FILES + "/*.txt")
    self.all_content = self.all_files_content


    print self.all_content()


  def all_files_content (self):
    all_files = self.all_files
    result = {}
    for chosen_file in all_files:
      result[chosen_file] = {'content': self.list_content(chosen_file)}

    return result

  def list_content(self, chosen_file):
    with open(chosen_file) as f:
      content = f.readlines()

    return content


if __name__ == '__main__':
    try:
        ParserFile()
    except Exception as e:
        print e