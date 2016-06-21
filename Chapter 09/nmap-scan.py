import nmap                         # import nmap.py module

nmap = nmap.PortScanner()
host = '127.0.0.1'
nmap.scan(host, '1-1024')
print nmap.command_line()
print nmap.scaninfo()

for host in nmap.all_hosts():
    print('Host : %s (%s)' % (host, nmap[host].hostname()))
    print('State : %s' % nmap[host].state())
for proto in nmap[host].all_protocols():
    print('Protocol : %s' % proto)

listport = nmap[host]['tcp'].keys()
listport.sort()

for port in listport:
    print('port : %s\tstate : %s' % (port, nmap[host][proto][port]['state']))
