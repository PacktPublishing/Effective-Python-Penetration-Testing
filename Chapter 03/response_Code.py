headers = {
	'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 7.0;
	Windows NT 5.1; .NET CLR 2.0.50727)'
}
r = urllib2.Request("http://somedomain.com/",
headers=headers)
u = urllib2.urlopen(r)
response = u.read()
