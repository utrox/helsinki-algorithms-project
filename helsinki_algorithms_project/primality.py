import random
from .erathostenes import sieve_of_erathostenes

DEFAULT_STEPS = 20
SMALLEST_PRIMES = sieve_of_erathostenes(4000)


def is_prime(n: int) -> bool:
    """
    Uses the Miller-Rabin probabilistic prime test
    to determine if the number is a prime or not.

    Arguments:
    n: int - the value you want to test the primality of.

    Returns:
    boolean - whether the number is (probably) a prime or not
    """
    # Handle easy and neccessary cases to optimize the function
    if n == 2 or n == 3:
        return True
    
    #################################################################
    # If the number is divisible by any of the smallest primes,     #
    # its not a prime number obviously. With this, we can speed up  #
    # the process of rejecting non-prime numbers, instead of always #
    # using Miller-Rabin from the start. This considerably          #
    # increases the speed of the function.                          #
    #################################################################
    if any([n % i == 0 and n != i for i in SMALLEST_PRIMES]) or n <= 1:
        return False
    k, m = factorize(n)
    return check_primality(n, k, m, DEFAULT_STEPS)


def factorize(n: int) -> tuple[int, int]:
    """
    Implements the factorization part of the Miller-Rabin primality test.

    (n - 1 = 2**k * m)

    Arguments: n: int - the number that we want to factorize

    Returns: tuple[int, int] - the value for k and m
    """
    steps = 0
    n = n - 1
    while n % 2 == 0:
        n //= 2 # integer division
        steps += 1

    return steps, n


def check_primality(n: int, k: int, m: int, steps: int) -> bool:
    """
    Recursive function that checks if the number is (probably) prime or not.

    Implements the steps 2, 3 and 4 of the Miller-Rabin primality probabilty test.
    Recursively calls itself with the amount of steps left to check.

    The more steps, the more accurate the test is.\n
    The probabilty of error is calculated with the formula (1/4)^steps.

    1 step: 25% error\n
    2 steps: 6.25% error\n
    3 steps: 1.56% error\n
    4 steps: 0.39% error\n
    5 steps: 0.0975% error\n
    10 steps: 0.000095% error\n
    20 steps: 0.0000000000000001% error\n

    Arguments:
    n: int - the number we want to check
    k: int - the value for k in the factorization
    m: int - the value for m in the factorization
    steps: int - the amount of steps left to check
    """
    for var in [n, k, m, steps]:
        if not isinstance(var, int):
            # Raise an error if any of the arguments is not an integer.
            # Because the numbers are possibly very large, using float
            # for instance would cause a significant loss of precision,
            # causing the function to not work properly.
            raise TypeError("All arguments must be integers.")

    if steps == 0:
        # The required amount of steps has been reached without
        # proving that n is composite, so it's probably a prime.
        return True

    # random.randint(x, y): x <= a <= y
    a = random.randint(2, n - 2)

    # x = a**m % n
    x = pow(a, m, n)
    if x == 1 or x == n - 1:
        # n might be a prime, so proceed with the next step
        return check_primality(n, k, m, steps - 1)

    m2 = m
    while m2 != n - 1:
        # x = x * x % n
        x = pow(x, 2, n)
        m2 *= 2
        if x == 1:
            # n is definitely composite, so return False
            return False
        elif x == n - 1:
            # n might be a prime, so proceed with the next step
            return check_primality(n, k, m, steps - 1)
    
    # n is definitely composite, so return False
    return False
