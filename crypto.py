#!/usr/bin/python

# import modules
import sys
from Crypto.Cipher import AES

version = sys.version
print(version)

obj = AES.new('1Secret2Squirrel', AES.MODE_CFB, 'This is an IV456')

securetext = obj.encrypt(version)
print('secure:', securetext)

obj2 = AES.new('1Secret2Squirrel', AES.MODE_CFB, 'This is an IV456')

plaintext = obj2.decrypt(securetext)
print('plain:', plaintext)
