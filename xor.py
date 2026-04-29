# from pwn import *

KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
KEY2_KEY1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
KEY2_KEY3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
FLAG_KEY1_KEY3_KEY2 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")


# takes binary strings and gives you the xor of them
def xor(str1, str2):
    return bytes(a ^ b for a, b in zip(str1, str2))

k1 = KEY1
k2 = xor(KEY1, KEY2_KEY1)
k3 = xor(KEY2_KEY3, k2)
flag = xor(xor(xor(FLAG_KEY1_KEY3_KEY2, k3), k2), k1)
print(flag)



