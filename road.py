from sage.all import *

p = 2**18*3**13-1

F = GF(p**2, names="i", modulus=[1,0,1])

E = EllipticCurve(F, [1,0])

def j(A,B):
    return 1728*4*A**3/(4*A**3+27*B**2)

t = 3*i**2 + 1

w = i*t

A = 1-5*t
B = -7*w

print(j(A,B))
