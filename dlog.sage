import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad

proof.all(False)

FLAG = b"crypto{?????????????????????????????????????????????????????????????}"

p = 2**127 - 1
F.<i> = GF(p^2, modulus=[1,0,1])
E = EllipticCurve(F, [1,0])
P, Q = E.gens()

a = randint(0, p) | 1
b = randint(0, p) | 1
c = randint(0, p) | 1
d = randint(0, p) | 1

R = a*P + b*Q
S = c*P + d*Q

def encrypt_flag(a, b, c, d):
    data_abcd = str(a) + str(b) + str(c) + str(d)
    key = SHA256.new(data=data_abcd.encode()).digest()[:128]
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct = cipher.encrypt(pad(FLAG, 16))

    return iv.hex(), ct.hex()

def decrypt_flag(a,b,c,d, ct, iv):
    data_abcd = str(a) + str(b) + str(c) + str(d)
    key = SHA256.new(data=data_abcd.encode()).digest()[:128]
    cipher = AES.new(key, AES.MODE_CBC, bytearray.fromhex(iv))
    pt = cipher.decrypt(bytearray.fromhex(ct))
    return pt

iv, ct = encrypt_flag(a, b, c, d)
P = E(24722427318870186874942502106037863239*i + 62223422355562631021732597235582046928, 66881667812593541117238448140445071224*i + 149178354082347398743922440593055790802)
Q = E(136066972787979381470429160016223396048*i + 52082760150043245190232762320312239515, 37290474751398918861353632929218878189*i + 89777436105166947842660822806860901885)
R = E(115434063687215369570994517493754451626*i + 158874018596958922133589852067300239562, 62259011436032820287439957155108559928*i + 81253318200557694469168638082106161224)
S = E(42595488035799156418773068781330714859*i + 113049342376647649006990912915011269440, 25404988689109287499485677343768857329*i + 125117346805247292256813555413193592812)

#iv = '6f5a901b9dc00aded4add3791812883b'
#ct = '56ecb68a90cad9787a24a4511720d40d625901577f6d0f1eef9fc34cf042709110cdc061fff91e934877674a30ed911283b83927dbcc270ae358d6b1fe2d5bed18ce1b02d8805de55e5b36deb0d28883'

print(P.weil_pairing(R, p+1))
print(Q.weil_pairing(R, p+1))
print(P.weil_pairing(P, p+1))
print(Q.weil_pairing(P, p+1))
