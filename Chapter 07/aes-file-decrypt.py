from Crypto.Cipher import AES
import os, random, struct

def decrypt_file(key, filename, chunk_size=24*1024):
        
    output_filename = os.path.splitext(filename)[0]

    with open(filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(output_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunk_size)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)

decrypt_file('abcdefghji123456', 'sample-file.txt.encrypted');