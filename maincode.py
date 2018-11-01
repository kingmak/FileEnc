import sys
from crypt import Crypt

#if len(sys.argv) != 3:
#    sys.exit('usage: {} file_to_encrypt password'.format(sys.argv[0]))

####################################################################################################
## file read
####################################################################################################
fileobj = open(sys.argv[1])
lines   = fileobj.read()
####################################################################################################

ccc = Crypt()
key = b"ahmed"
msg = b"hammad"

encrypted = ccc.encrypt(key, msg)    
decrypted = ccc.decrypt(key, encrypted)

print(encrypted)
print(decrypted)