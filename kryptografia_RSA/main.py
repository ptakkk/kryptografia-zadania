import math

#p = 2213
#q = 1049
p = 31
q = 19
#p = 47
#q = 71

n = p * q
phi = (p - 1) * (q - 1)


def coprime_number():
    e = 2  # Start with the smallest possible candidate
    while math.gcd(e, phi) != 1:
        e += 1
    return e

e = coprime_number()

"""
def modulo_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q1 = a // m
        m, a = a % m, m
        x0, x1 = x1 - q1 * x0, x0
    return x1 + m0 if x1 < 0 else x1
"""
#d = modulo_inverse(e, phi)
d = pow(e, -1, phi)

public_key = (e, n)
private_key = (d, n)

message = "58917304286731290574021639458203719486521307945628"
#message = "6882326879666683"
#message = "8587879809091235"
chunks = [(message[i]) for i in range(len(message))]

encrypted_message = []


def encryption():
    #e, n = public_key
    for chunk in chunks:
        chunk_int = int(chunk)
        encrypted_chunk = pow(chunk_int, e, n)
        print(encrypted_chunk)
        encrypted_message.append(encrypted_chunk)

decrypted_message = []


def decryption():
    for dchunk in encrypted_message:
        dchunk_int = int(dchunk)
        decrypted_chunk = pow(dchunk_int, d, n)
        print(decrypted_chunk)
        decrypted_message.append(decrypted_chunk)


if __name__ == '__main__':
    print(e, d, phi)
    print(chunks)
    encryption()
    print(encrypted_message)
    decryption()
    print(decrypted_message)
