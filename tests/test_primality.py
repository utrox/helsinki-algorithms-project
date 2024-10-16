import json
import pytest
from helsinki_algorithms_project.primality import is_prime, factorize, check_primality


def test_factorization():
    values = json.load(open("tests/data/test_factorization_values.json"))
    for key, (k, m) in values.items():
        assert (factorize(int(key)) == (k, m), 
                f"Factorization failed for {key}. Expected: {k, m}, got: {factorize(int(key))}")
        

def test_primality():
    values = json.load(open("tests/data/test_prime_values.json"))
    for i in range(-10, values[-1]):
        prime = is_prime(i)
        if prime and i not in values:
            assert False, f"{i}, result is PRIME, but is NOT acutally a prime."
        elif not prime and i in values:
            assert False, f"{i}, result is NOT PRIME, but is actually a prime."
        

def test_check_primality_only_accepts_integers():
    """Check that the function only accepts integers as arguments, for all values."""
    values = [1, 1, 1, 1.0]
    for _ in range(len(values)):
        with pytest.raises(TypeError):
            check_primality(*values)
        # Rotates the list so that the first value becomes the last one.
        values.append(values.pop(0))