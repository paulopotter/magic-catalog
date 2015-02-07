#! /usr/bin/env python
# coding:utf-8

from config import *
from glob import glob

class ParserFile:

  def __init__(self):
    self.all_files = glob(PATH_FILES + "/*.txt")
    self.all_content = self.all_files_content
    # print self.find_card(self.list_content(self.all_files[0])[3]['card_name'])[0]

  def all_files_content (self):
    all_files = self.all_files
    result = {}
    for chosen_file in all_files:
      result[chosen_file] = {'content': self.list_content(chosen_file)}

    return result

  def list_content(self, chosen_file):
    result =[]
    with open(chosen_file) as f:
      content = f.readlines()
    for file_line in range(len(content)):
      line = content[file_line].strip()
      line_split = line.split('[')
      card_name = line_split[0]
      card_quant = line_split[1]
      result.append({
          'card_name': card_name,
          'quant': card_quant,
          'links_to_search': self.find_card(card_name),
        })

    return result

  def find_card(self, card_name):
    sites = PAGE_CONFIG.keys()
    result =[]
    for page in sites:
      link = PAGE_CONFIG[page]['search_format'] .format(card_name).strip()
      result.append(link.replace(' ', '%20'))

    return result
