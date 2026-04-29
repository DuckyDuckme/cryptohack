def xor(str1, str2):
    return bytes(a ^ b for a, b in zip(str1, str2))

h = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
print(h)



key = [ord(c) for c in "myXORkey"]

print(bytes(key))

print(len(key))
l = int(len(h)/len(key)) + 1
# print(len(h))

key = bytes(l*key)
print(key)
flag = xor(h, key)

print(flag)
