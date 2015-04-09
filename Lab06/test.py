#! /usr/bin/env python3.4
import re

def getGenres():
    with open('books.xml', 'r') as f:
        lines = f.read()
    genres = re.findall(r'<genre>(\w*)</genre>',lines)
    genres.sort()
    return genres

def getAuthorOf(bookname):
    with open('books.xml', 'r') as f:
        lines = f.read()
    author = re.findall(r'<author>(.*?)</author>\n[\t\s]*<title>'+bookname+r'</title>',lines)
    if not author:
        return None
    return author

def getBookInfo (bookID):
    with open('books.xml', 'r') as f:
        lines = f.read()
    out = re.findall(r'<book id=\"'+bookID+r'\">[\n\t\s]*<author>(.*?)</author>\n[\t\s]*<title>(.*?)</title>',lines)
    if out:
        author, title = out[0]
        return title, author
    else:
        return None

def getBooksBy(authorName):
    with open('books.xml', 'r') as f:
        lines = f.read()
    books = re.findall(r'<author>'+authorName+r'</author>\n[\t\s]*<title>(.*?)</title>',lines)
    if books:
        return books
    else:
        return []

def getBooksBelow(bookPrice):
    namelist = []
    with open('books.xml', 'r') as f:
        lines = f.read()
    price = re.findall(r'<title>(.*?)</title>\n[\t\s]*<genre>(.*?)</genre>\n[\t\s]*<price>(.*?)</price>',lines)
    for l in price:
        name,_,p = l
        if float(p) < bookPrice:
            namelist += [name]
    return namelist

def searchForWord(word):
    namelist = []
    with open('books.xml', 'r') as f:
        lines = f.read()
    ww = re.findall(r'<title>(.*?'+word+r'.*?)</title>|<description>.*?'+word+r'.*?</description>',lines)
    return ww


if __name__ == "__main__":
    getGenres()
    getAuthorOf('Maeve Ascendant')
    T = getBookInfo('bk101')
    getBooksBy('Corets, Eva')
    getBooksBelow(50)
    searchForWord('a')
   # <book id="bk101">
   #    <author>Gambardella, Matthew</author>
   #    <title>XML Developer's Guide</title>
   #    <genre>Computer</genre>
   #    <price>44.95</price>
   #    <publish_date>2000-10-01</publish_date>
   #    <description>An in-depth look at creating applications
   #    with XML.</description>
   # </book>