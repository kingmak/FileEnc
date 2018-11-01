import sys
from crypt import Crypt

if len(sys.argv) != 3:
    sys.exit("usage: {} file_to_encrypt password".format(sys.argv[0]))

####################################################################################################
## file read
####################################################################################################
fileobj = open(sys.argv[1])
msg     = bytes(fileobj.read(), "utf-8")
####################################################################################################

ccc = Crypt()
key = bytes(sys.argv[1], "utf-8")

encrypted = ccc.encrypt(key, msg)    
decrypted = ccc.decrypt(key, encrypted)

print(encrypted)
print(decrypted)