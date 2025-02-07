#!/usr/bin/env python3
import timeit
import json
import time

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def benchmark_fib():
    n = 30
    iterations = 10
    total_time = timeit.timeit(lambda: fib(n), number=iterations)
    return total_time

if __name__ == "__main__":
    runtime = benchmark_fib()
    result = {
        "benchmark": "fib_benchmark",
        "runtime": runtime,
        "iterations": 10,
        "timestamp": time.time()
    }
    print(json.dumps(result))
