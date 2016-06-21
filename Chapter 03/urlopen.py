	import urllib
	url = urllib.urlopen("http://packtpub.com/")
	data = url.read()
	print data
