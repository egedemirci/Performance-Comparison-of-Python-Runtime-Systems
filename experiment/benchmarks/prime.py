#!/usr/bin/env python3

import time
import json
from memory_profiler import profile 

def is_prime(n):
    """
    Basic primality test with O(sqrt(n)) complexity.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@profile
def prime_count(limit):
    """
    Counts how many primes exist up to `limit`.
    """
    count = 0
    for x in range(1, limit + 1):
        if is_prime(x):
            count += 1
    return count

def benchmark_cpu_intensive(limit=100000):
    """
    A CPU-intensive benchmark that counts primes up to `limit`.
    Returns the number of primes found and the total runtime.
    """
    start_time = time.time()
    total_primes = prime_count(limit)
    end_time = time.time()
    return total_primes, end_time - start_time

if __name__ == "__main__":
    limit = 5000000
    primes, runtime = benchmark_cpu_intensive(limit)
    
    result = {
        "benchmark": "cpu_bound_prime_count",
        "limit": limit,
        "prime_count": primes,
        "runtime": runtime,
        "timestamp": time.time()
    }
    print(json.dumps(result))
