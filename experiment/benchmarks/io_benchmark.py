#!/usr/bin/env python3
import timeit
import json
import time
import tempfile
import os

def benchmark_io():
    iterations = 10
    data = "Hello, world!\n" * 10000
    
    def io_task():
        with tempfile.NamedTemporaryFile(delete=False) as tf:
            tf.write(data.encode('utf-8'))
            filename = tf.name
        with open(filename, 'r') as f:
            _ = f.read()
        os.remove(filename)
    
    total_time = timeit.timeit(io_task, number=iterations)
    return total_time

if __name__ == "__main__":
    runtime = benchmark_io()
    result = {
        "benchmark": "io_benchmark",
        "runtime": runtime,
        "iterations": 10,
        "timestamp": time.time()
    }
    print(json.dumps(result))
