#!/usr/bin/python
import sys
import urllib
sys.path.append("./")

from bs4 import BeautifulSoup
html = urllib.urlopen("http://www.tertuliaconscienciologia.org/index.php?option=com_content&task=view&id=45&Itemid=59")
bsObj = BeautifulSoup(html.read(), 'html.parser')
LI=bsObj.find_all('li')

list1 = ' '.join(sys.argv[1:])

def main():
  for x in range(0,len(LI)):
    A = LI[x].a
    # print A
    if A != None:
    	link = A.get('href')
    	if link.find("youtu") == -1:
           print link

if __name__ == '__main__':
    main()
