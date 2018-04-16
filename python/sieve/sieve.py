def sieve(limit):
    non_primes = set(range(2, limit+1))
    primes = set()
    while len(non_primes) > 0:
        prime = min(non_primes)
        primes.add(prime)
        non_primes = non_primes - set(range(prime, limit+1, prime))

    return sorted(primes)
