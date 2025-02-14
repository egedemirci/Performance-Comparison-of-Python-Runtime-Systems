#!/usr/bin/env jython
import time
import json
from java.util import HashMap

iterations = 10

def dictionary_benchmark():
    # Prepare test data: keys are strings and values are integers.
    num_entries = 100000
    keys = [str(i) for i in range(num_entries)]
    values = [i for i in range(num_entries)]
    
    total_time = 0.0
    for _ in range(iterations):
        hm = HashMap()
        start = time.time()
        for k, v in zip(keys, values):
            hm.put(k, v)
        end = time.time()
        total_time += (end - start)
    return total_time

if __name__ == "__main__":
    runtime = dictionary_benchmark()
    result = {
        "benchmark": "jython_dictionary_benchmark",
        "runtime": runtime,
        "iterations": iterations,
        "timestamp": time.time()
    }
    print(json.dumps(result))
