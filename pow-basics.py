from hashlib import sha256

inp = 'Hallo Welt'
current_hash = sha256(inp.encode('utf-8')).hexdigest()

diff = 2
nonce = 0

while not current_hash.startswith('0' * diff):
    nonce += 1 
    to_be_hashed = 'Inhalt / Daten' + str(nonce)
    current_hash = sha256(to_be_hashed.encode('utf-8')).hexdigest()
    print('current hash: ', current_hash)


print('nonce: ', nonce)
print('hash: ', current_hash)


