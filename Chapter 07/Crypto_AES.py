from Crypto.Cipher import AES
encrypt_AES = AES.new('secret-key-12345', AES.MODE_CBC, 'This is an IV456')
message = "This is message "
ciphertext = encrypt_AES.encrypt(message)
print ciphertext
decrypt_AES = AES.new('secret-key-12345', AES.MODE_CBC, 'This is an IV456')
message_decrypted =  decrypt_AES.decrypt(ciphertext)
print message_decrypted
