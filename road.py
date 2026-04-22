from sage.all import *

p = 2**18*3**13-1

F = GF(p**2, name="i", modulus=[1,0,1])
i = F.gens()[0]

A = F(1)
B = F(0)
E = EllipticCurve(F, [A, B])
P = E(357834818388*i + 53943911829, 46334220304*i + 267017462655)
#P = E(i,0)

def two_isogeny(P, A, B):
    assert P.order() % 2 == 0
    xP = P[0]
    yP = P[1]

    tP = 3*xP**2 + A
    uP = 2*yP**2
    wP = uP + tP*xP


    new_A = A - 5*tP
    new_B = B - 7*wP

    return new_A, new_B


# take point of order three
def three_isogeny(Q, A, B):
    #assert Q.order() % 3 == 0

    t = F(0)
    w = F(0)

    for P in [Q, 2*Q]:
        xP = P[0]
        yP = P[1]

        tP = 3*xP**2 + A
        uP = 2*yP**2
        wP = uP + tP*xP
        t += tP
        w += wP

    new_A = A - 5*t
    new_B = B - 7*w

    return new_A, new_B#, x_new_Q

def prime_isogeny(P):
    return

def composite_isogenies(P):
    # P is of order p^e, we compute the isogeny
    return


pts = [P*3**i for i in range(1,14)]
print(pts)
for j in range(1,14):
    print(j, A,B, pts[-j])
    A, B = three_isogeny(pts[-j], A, B)

def j(A,B):
    return 1728*4*A**3/(4*A**3 + 27*B**2)


print(A)
print(j(A,B))
print([factor(P.order()) for P in pts])
