from metasploit.msfrpc import MsfRpcClient
from metasploit.msfconsole import MsfRpcConsole

client = MsfRpcClient('123456', user='msf')

print dir(console)

auxilary = client.modules.auxiliary

for i in auxilary:
	print "\t%s" % i

scan = client.modules.use('auxiliary', 'scanner/ssh/ssh_version')

scan.description

scan.required

scan['VERBOSE'] = True
scan['RHOSTS'] = '192.168.1.119'

print scan.execute()

console = MsfRpcConsole(client)

console.execute('use scanner/ssh/ssh_version')
console.execute('set RHOSTS 192.168.1.119')
console.execute('set VERBOSE True')
console.execute('run')
