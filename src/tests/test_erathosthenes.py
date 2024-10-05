import json
from erathostenes import sieve_of_erathostenes

def test_primality():
    TEST_TO = 10000
    values = json.load(open("tests/data/test_prime_values.json"))
    primes = sieve_of_erathostenes(TEST_TO)
    for i in range(-10, TEST_TO):
        if i in primes and i not in values:
            assert False, f"{i}, result is PRIME, but is NOT acutally a prime."
        elif i not in primes and i in values:
            assert False, f"{i}, result is NOT PRIME, but is actually a prime."