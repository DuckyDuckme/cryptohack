import base64
import python-pwntools

input = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
dec = bytes.fromhex(input)
b = base64.b64encode(dec)
print(str(b))
