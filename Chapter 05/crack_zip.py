import zipfile

filename = 'test.zip'
dictionary = 'passwordlist.txt'

password = None
file_to_open = zipfile.ZipFile(filename)
with open(dictionary, 'r') as f:
	for line in f.readlines():
		password = line.strip('\n')
		try:
			file_to_open.extractall(pwd=password)
			password = 'Password found: %s' % password
			print password
		except:
			pass