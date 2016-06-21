from bs4 import BeautifulSoup
import re

parse = BeautifulSoup('<html><head><title>Title of the page</title></head><body><p id="para1" align="center">This is a paragraph<b>one</b><a href="http://example1.com">Example Link 1</a> </p><p id="para2">This is a paragraph<b>two</b><a href="http://example.2com">Example Link 2</a></p></body></html>')

print parse.prettify()

<html>
 <head>
  <title>
   Title of the page
  </title>
 </head>
 <body>
  <p align="center" id="para1">
   This is a paragraph
   <b>
    one
   </b>
   <a href="http://example1.com">
    Example Link 1
   </a>
  </p>
  <p id="para2">
   This is a paragraph
   <b>
    two
   </b>
   <a href="http://example.2com">
    Example Link 2
   </a>
  </p>
 </body>
</html>

