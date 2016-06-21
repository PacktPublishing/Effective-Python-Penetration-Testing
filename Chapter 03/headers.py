import urllib
url = urllib.urlopen("http://packtpub.com/")
response_headers = url.info()
#print response_headers
#print response_headers.keys()
print response_headers['server']
