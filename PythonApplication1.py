import hashlib
import re
info = input("message:")
sha512_hash = hashlib.sha512(info.encode()).hexdigest()
print(sha512_hash)
name_long = int(input("name_long:"))
name = sha512_hash[0:name_long]
print("name:"+name)
key_long = int(input("key long:"))
sha512_hash = sha512_hash[::-1]
print("key:"+sha512_hash[0:key_long])
pin_sha512_hash = re.sub(r"\D", "", sha512_hash)
print("pin:"+pin_sha512_hash[0:6])