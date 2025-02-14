#!/usr/bin/env python3
import time
import json

def dictionary_benchmark():
    iterations = 10
    # Prepare test data: keys are strings and values are integers.
    num_entries = 100000
    keys = [str(i) for i in range(num_entries)]
    values = [i for i in range(num_entries)]
    
    total_time = 0.0
    for _ in range(iterations):
        hm = {}  # Python built-in dictionary
        start = time.time()
        for k, v in zip(keys, values):
            hm[k] = v
        end = time.time()
        total_time += (end - start)
    return total_time, iterations

if __name__ == "__main__":
    runtime, iterations = dictionary_benchmark()
    result = {
        "benchmark": "python_dictionary_benchmark",
        "runtime": runtime,
        "iterations": iterations,
        "timestamp": time.time()
    }
    print(json.dumps(result))
