#!/usr/bin/env python3
import timeit
import json
import time
import tempfile
import os
import tracemalloc


def benchmark_io():
    iterations = 100
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
    tracemalloc.start()
    runtime = benchmark_io()
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()
    result = {
        "benchmark": "io_benchmark",
        "runtime": runtime,
        "iterations": 100,
        "timestamp": time.time()
    }
    print(json.dumps(result))
