import hmac
import hashlib

digest_maker = hmac.new('secret-key', '', hashlib.sha256)

f = open('sample-file.txt', 'rb')
try:
    while True:
        block = f.read(1024)
        if not block:
            break
        digest_maker.update(block)
finally:
    f.close()

digest = digest_maker.hexdigest()
print digest