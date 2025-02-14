#!/usr/bin/env python3
import timeit
import random
import json
import time

def benchmark_sort():
    iterations = 10
    size = 100000
    setup_code = "import random; data = [random.random() for _ in range({})]".format(size)
    stmt = "sorted(data)"
    total_time = timeit.timeit(stmt=stmt, setup=setup_code, number=iterations)
    return total_time

if __name__ == "__main__":
    runtime = benchmark_sort()
    result = {
        "benchmark": "sort_benchmark",
        "runtime": runtime,
        "iterations": 10,
        "timestamp": time.time()
    }
    print(json.dumps(result))
