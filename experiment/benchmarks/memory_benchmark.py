#!/usr/bin/env python3
import timeit
import json
import time

def benchmark_memory():
    iterations = 10
    size = 1000000
    stmt = "[x for x in range({})]".format(size)
    total_time = timeit.timeit(stmt=stmt, number=iterations)
    return total_time

if __name__ == "__main__":
    runtime = benchmark_memory()
    result = {
        "benchmark": "memory_benchmark",
        "runtime": runtime,
        "iterations": 10,
        "timestamp": time.time()
    }
    print(json.dumps(result))
