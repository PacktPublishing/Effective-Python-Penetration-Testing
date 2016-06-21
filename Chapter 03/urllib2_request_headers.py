headers = {
	'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0'
}
request = urllib2.Request("http://packtpub.com/", headers=headers)
url = urllib2.urlopen(request)
response = u.read()	
