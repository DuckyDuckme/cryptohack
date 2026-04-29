input = "RTOQDLD SQNOGX BZRTZK BNSSNM"

inputs = input.split(" ")
print(inputs)

l = len(input)
for i in range(26):
    for inp in inputs:
        lst = list(inp)

        possible = [chr(((ord(letter) + i) % 26) + 65) for letter in lst]
        print(''.join(possible))




