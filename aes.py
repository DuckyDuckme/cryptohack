# takes binary strings and gives you the xor of them
def xor(str1, str2):
    return bytes(a ^ b for a, b in zip(str1, str2))


def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    res = []
    for i in range(4):
        for j in range(4):
            char = matrix[i][j]
            res.append(char)

    return bytes(res)

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]


print(matrix2bytes(bytes2matrix(bytes("texttexttexttext", "utf-8"))))
print(matrix2bytes(matrix))

########### add round key ##############

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def add_round_key(s, k):
    S = matrix2bytes(s)
    K = matrix2bytes(k)
    print(S, "\n", K)
    return xor(S, K)

res = add_round_key(state, round_key)
print(res)