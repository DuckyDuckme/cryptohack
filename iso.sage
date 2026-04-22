
p = 1912812599
F = GF(p)
R.<x> = PolynomialRing(F, 'x')
#R.<a,b> = PolynomialRing(F, 'a, b')

#var('x')



def img():
    P = (48622,27709)
    xp = F(P[0])
    yp = F(P[1])
    Q = (9460,13819)
    xq = F(Q[0])
    yq = F(Q[1])



    #var('a b')
    f = yp^2-xp^3-a*xp -b
    g = yq^2-xq^3-a*xq -b

    print(f,g)

    I = Ideal(f, g)
    d = I.variety()[0]
    A = d[a]
    B = d[b]

    E = EllipticCurve(F, [A,B])
    print(E)

    P = E(P)
    Q = E(Q)

    print((P+Q).x())

def montgomery():
    a = 312589632
    b = 654443578
    f = x^3 + a*x + b

    d = f.roots()

    r = d[0][0]

    y = x+r
    
    g = y^3 + a*y + b
    print(g)
    coefs = g.coefficients()
    const = F(coefs[0])
    A = F(coefs[1])

    h = x^4 - const
    d = h.roots()

    print(d)
    u = d[1][0]

    y = (x+r)*u^(-2)
    g = y^3 + a*y + b
    print(g)
    print(A/u^2)


def dlog(P,Q,R,n):
    # P,Q the basis, n = p + 1 is the order of each of them
    # 
    for a in range(n):
        for b in range(n):
            T = a*P + b*Q









