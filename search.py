#! /usr/bin/env python
# coding:utf-8

from parser_file import ParserFile
import urllib

class Search:

  def __init__(self):
    self.all_files_content = ParserFile().all_files_content()
    link_url = self.search_by_file(self.files_name()[0])[0]


  def files_name(self):
    all_files =self.all_files_content
    files_name = []
    for keys in all_files.keys():
      files_name.append(keys)

    return files_name

  def search_by_file(self, files_name):
    result = []
    for cards in self.all_files_content[files_name]['content']:
      result.append(cards['links_to_search'][0])

    return result

  def open_url(self, url):
    f = urllib.urlopen(url)
    return f.read()

if __name__ == '__main__':
    try:
        Search()
    except Exception as e:
        print e