Import peutils
Import pefile
pe = pefile.PE('md5sum-packed.exe')

signatures = peutils.SignatureDatabase('http://reverse-engineering-scripts.googlecode.com/files/UserDB.TXT')
matches = signatures.match(pe, ep_only = True)
print matches
