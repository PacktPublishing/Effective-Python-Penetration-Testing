import pyclamd


try:
	clamd = pyclamd.ClamdUnixSocket()
	# test if server is reachable
	clamd.ping()
except pyclamd.ConnectionError:
	# if failed,  test for network socket
	clamd = pyclamd.ClamdNetworkSocket()
	try:
		clamd.ping()
	except pyclamd.ConnectionError:
		raise ValueError('could not connect to clamd server either by unix or network socket')

print(clamd.version())
print(clamd.scan_file('path-to-file-or-folder-to-scan'))
