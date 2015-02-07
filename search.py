#! /usr/bin/env python
# coding:utf-8

from parser_file import ParserFile
import urllib

class Search:

  def __init__(self):
    self.all_files_content = ParserFile().all_files_content()

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

  def  find_card(self, html):
    html_begin = html.find("<table border='0' cellpadding='1' cellspacing='1' width='100%' style='margin-top:4px;'>")
    html_strip_begin = html[html_begin:]

    html_end = html_strip_begin.find("</table>")
    html_strip_end = html[html_begin:(html_begin + html_end)]

    html_find_attr_begin = html_strip_end.split("<tr>\r\n                                            <td class='advs' width='105'>")
    html_find_attr_end = []

    for bla in html_find_attr_begin:
      html_find_attr_end.append(bla.split("</td>\r\n                                            <td class='advv'>"))

    resoluto =[]
    result = []
    for attr in html_find_attr_end[1]:
      resoluto.append(attr.split("</td>\r\n                                        </tr>")[0] )

    result.append({resoluto[0].split("&nbsp;")[0]: resoluto[1].strip()})

    return result

  def return_matches(self):
    result = {}
    print '\r['

    for i,link_url in enumerate(self.search_by_file(self.files_name()[0])):
      new_name_card = self.find_card( self.open_url(link_url))
      result[i] = [new_name_card[0], {'url': link_url}]
      print '\r .'

    print ']'
    return result


if __name__ == '__main__':
    try:
        Search()
    except Exception as e:
        print e

