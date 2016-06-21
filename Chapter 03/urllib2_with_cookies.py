fields = {
'name' : 'sean',
'password' : 'password!',
'login' : 'LogIn'
}
opener = urllib2.build_opener(
	urllib2.HTTPCookieProcessor()
)
request = urllib2.Request(
	"http://example.com/login",
	urllib.urlencode(fields))

url = opener.open(request)
response = url.read()

url = opener.open("http://example.com/dashboard")
response = url.read()
