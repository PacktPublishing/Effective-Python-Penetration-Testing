import mechanize

url = "http://www.webscantest.com/datastore/search_by_id.php"
browser = mechanize.Browser()
attackNumber = 1
with open('attack-vector.txt') as f:
    for line in f:
    	browser.open(url)
	browser.select_form(nr=0)
    	browser["id"] = line
    	res = browser.submit()
	content = res.read()
	output = open('response/'+str(attackNumber)+'.txt', 'w')
	output.write(content)
	output.close()
	print attackNumber
	attackNumber += 1
	
