import secrets

from primality import is_prime
from keygen import (
    RSAKeyType,
    write_key_to_file, 
    get_base64_key, 
    read_key_from_file, 
    decode_base64_key
)

def generate_prime(bits: int = 1024):
    """Returns a prime number with the specified amount of bits."""
    while True:
        candidate = secrets.randbits(bits)
        if is_prime(candidate):
            return candidate


def generate_rsa_keypairs(bits: int = 1024):
    """
    Returns a pair of RSA keys, public and private. 
    Both keys are tuples, containing an exponent and modulus.
    """
    p, q = generate_prime(bits), generate_prime(bits)
    
    # Make sure p and q are not the same.
    while p == q:
        q = generate_prime(bits)
    
    n = p * q

    phi_n = (p - 1) * (q - 1)
    
    # Check the thread below for explanation of why this value is hardcoded.
    # https://crypto.stackexchange.com/questions/3110/impacts-of-not-using-rsa-exponent-of-65537
    public_exponent = 65537
    
    private_exponent = pow(public_exponent, -1, phi_n)
    return (public_exponent, n), (private_exponent, n)


if __name__ == "__main__":
    import os
    
    # Make the output folder, if it does not exist yet.
    os.makedirs("output", exist_ok=True)

    (e, n), (d, n) = generate_rsa_keypairs()
    public_base64: str = get_base64_key(e, n, RSAKeyType.PUBLIC)
    private_base64: str = get_base64_key(d, n, RSAKeyType.PRIVATE)

    write_key_to_file("output/public.der", public_base64, RSAKeyType.PUBLIC)
    write_key_to_file("output/private.der", private_base64, RSAKeyType.PRIVATE)

    read_public = read_key_from_file("output/public.der")
    read_private = read_key_from_file("output/private.der")

    (e1, n1) = decode_base64_key(read_public, RSAKeyType.PUBLIC)
    (d1, n2) = decode_base64_key(read_private, RSAKeyType.PRIVATE) 
    assert e == e1
    assert d == d1
    assert n == n1
    assert n == n2
