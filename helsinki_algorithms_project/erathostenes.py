def sieve_of_erathostenes(n: int) -> list[int]:
    """Returns a list of all prime numbers between 0 and n."""
    if n < 2:
        return []
    
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    numbers = [2] + list(range(3, n + 1, 2))
    
    for i in numbers:
        if not is_prime[i]:
            continue

        multiplier = 2
        multiplied = i * multiplier
        while multiplied <= n:
            is_prime[multiplied] = False
                
            multiplier += 1
            multiplied = i * multiplier
    return [i for i in range(2, n + 1) if is_prime[i]]
