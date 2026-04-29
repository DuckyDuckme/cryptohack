p = 9739

def inv(a, p):
    return pow(a, -1, p)

def curve_eq(S):
    x = S[0]
    y = S[1]
    return (y**2-x**3-497*x-1768) % p == 0

def point_addition(P, Q, a = 497):
    if P is None:
        return Q
    if Q is None:
        return P

    x_1 = P[0]
    y_1 = P[1]
    x_2 = Q[0]
    y_2 = Q[1]

    if x_1 == x_2 and y_1 == -y_2:
        return None
    else:
        if x_1 != x_2 or y_1 != y_2:
            l = (y_2 - y_1) % p
            l *= inv(x_2 - x_1, p)
        else:
            l = (3*x_1**2 + a)*inv(2*y_1,p)
        x_3 = (l**2-x_1-x_2) % p
        y_3 = (l*(x_1-x_3) - y_1) % p

    return x_3, y_3

def DAA(P, n):
    Q = P
    R = None
    while n > 0:
        if n % 2 == 1:
            R = point_addition(Q, R)
        Q = point_addition(Q, Q)
        n //= 2

    return R

P = (2339,2213)
Q = DAA(P, 7863)
print(Q)
print(curve_eq(Q))