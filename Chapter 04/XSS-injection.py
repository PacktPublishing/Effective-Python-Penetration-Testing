import mechanize

url = "http://www.webscantest.com/crosstraining/aboutyou.php"
browser = mechanize.Browser()
attackNumber = 1
with open('XSS-vectors.txt') as f:
    for line in f:
    	browser.open(url)
	browser.select_form(nr=0)
    	browser["fname"] = line
    	res = browser.submit()
	content = res.read()
	#  check the attack vector is printed in the response.
    	if content.find(line) > 0:
    		print "Possible XXS"
    	
	output = open('response/'+str(attackNumber)+'.txt', 'w')
	output.write(content)
	output.close()
	print attackNumber
	attackNumber += 1
	
