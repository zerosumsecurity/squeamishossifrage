
def gen_backdoor():
    backdoor = 2
    for _ in range(24):
        p = random.randint(1,2**20)
        p = gmpy.next_prime(p)
        backdoor *= p
    return backdoor


def gen_rsa(num_bits, backdoor):
    found = False
    while not found:
        p = random.randint(2**(num_bits//2-1), 2**(num_bits//2))
        p = gmpy.next_prime(p)
        q = p+backdoor
        if gmpy.is_prime(q):
            found = True
    phi = (p-1)*(q-1)
    d = gmpy.invert(65537, phi)
    N = p*q
    return N,p,q,d