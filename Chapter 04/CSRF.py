import mechanize

cookies = mechanize.CookieJar()

cookie_opener = mechanize.build_opener(mechanize.HTTPCookieProcessor(cookies))

mechanize.install_opener(cookie_opener) 

url = "http://www.webscantest.com/crosstraining/aboutyou.php"


res = mechanize.urlopen(url)
content = res.read()
	
  
	
