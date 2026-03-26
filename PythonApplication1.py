import hashlib
info = input("message:")
sha512_hash = hashlib.sha512(info.encode()).hexdigest()
print(sha512_hash)
name_long = int(input("name_long:"))
name = sha512_hash[0:name_long]
print(name)
key_long = int(input("key long:"))
sha512_hash = sha512_hash[::-1]
print(sha512_hash[0:key_long])