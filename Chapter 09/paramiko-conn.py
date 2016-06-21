import os
import paramiko

host = 'localhosr'
username = 'root'
password = '123456'

ssh = paramiko.SSHClient()
parmiko.util.log_to_file(log_filename)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print "creating connection"
    ssh.connect(host, username=username, password=password)
    print "connected"
    yield ssh
finally:
    print "closing connection"
    ssh.close()
    print "closed"
