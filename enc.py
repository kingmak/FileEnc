import sys

if len(sys.argv) != 3:
    sys.exit('usage: {} file_to_encrypt password'.format(sys.argv[0]))

import hashlib    

salt   = 'hammad'
key    = (salt + sys.argv[2]).encode('utf-8')
shakey = hashlib.sha512(key).hexdigest()

print(shakey)