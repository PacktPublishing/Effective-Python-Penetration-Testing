import urllib
fields = {
	'name' : 'Sean',
	'email' : 'Sean@example.com'
}
parms = urllib.urlencode(fields)
print parms
