from sympy import isprime, totient, factorint


def is_primitive_root(g, n, factors):
    for p in factors:
        if pow(g, int(totient(n)//p), n) == 1:
            return False
    return True


def find_primitive_root(n):
    if not isprime(n):
        return None  # n must be prime for a primitive root to exist

    factors = factorint(totient(n)).keys()
    for g in range(2, n):
        if is_primitive_root(g, n, factors):
            return g
    return None

n = 17   # then g = 3
primitive_root = find_primitive_root(n)

x = 7  # alice chooses a random total number (secret)
X = pow(primitive_root, x, n)

y = 4  # bob chooses a random total number (secret)
Y = pow(primitive_root, y, n)

k_alice = pow(Y, x, n)
k_bob = pow(X, y, n)



if __name__ == "__main__":

    print(f"A primitive root modulo {n} is: {primitive_root}")

    print(X)
    print(Y)

    print(k_alice)
    print(k_bob)
