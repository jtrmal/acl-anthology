#!/bin/env python3
# need: BeautifulSoup4, lxml
# i.e.
#      pip3 install lxml
#      pip3 install beautifulsoup4

from bs4 import BeautifulSoup as xml


class GenericCitationParser:
    def __init__(self):
        pass

    @staticmethod
    def identify(xml):
        return True

class WithBookInfoCitationParser(GenericCitationParser):
    def __init__(self):
        pass

    @staticmethod
    def identify(xml):
        maybe_book_id = xml.volume.findAll(attrs={"id" : "1000"})
        if not maybe_book_id:
            return False
        book_id = maybe_book_id[0]
        if (book_id.bibtype is not None) and (book_id.bibtype.string == "book"):
            return True
        return False


with open('./acl-anthology/import/P18.xml') as f:
    cite = xml(f, 'lxml-xml')
    WithBookInfoCitationParser.identify(cite)
