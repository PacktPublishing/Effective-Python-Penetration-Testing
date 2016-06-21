import os,sys
from PIL import Image
from PIL.ExifTags import TAGS

for (i,j) in Image.open('image.jpg')._getexif().iteritems():
        print '%s = %s' % (TAGS.get(i), j)
