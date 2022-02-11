

def generate_prime(num_bits):
    # make sure we start with a composite number so we are guaranteed to
    # enter the main loop and get a collatz prime
    p = random.randint(1, 2**(num_bits/2))**2
    # enter the collatz (3n+1)-loop
    while not gmpy.is_prime(p):
        if 0 == p%2:
            p = p//2
        else:
            p = 3*p+1
        # restart if the number of bits fails out of range
        if ( (p.bit_length() < num_bits - 32) or (p.bit_length() > num_bits + 32) ):
            p = random.randint(1, 2**(num_bits/2))**2
    return p
