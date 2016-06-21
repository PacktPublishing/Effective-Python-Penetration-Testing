import hmac

hmac_md5 = hmac.new('secret-key')

f = open('sample-file.txt', 'rb')
try:
    while True:
        block = f.read(1024)
        if not block:
            break
        hmac_md5.update(block)
finally:
    f.close()

digest = hmac_md5.hexdigest()
print digest