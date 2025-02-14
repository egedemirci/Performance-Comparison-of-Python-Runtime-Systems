#!/usr/bin/env jython
import time
import json
from java.util.concurrent import Executors, TimeUnit

# Define iterations explicitly.
iterations = 10

def async_task():
    # A simple CPU-bound task: compute the sum of numbers from 1 to 1000.
    s = 0
    for i in range(1, 1001):
        s += i
    return s

def benchmark_async():
    n_tasks = 1000  # number of tasks per iteration
    executor = Executors.newFixedThreadPool(4)
    start = time.time()
    for _ in range(iterations):
        futures = []
        for i in range(n_tasks):
            future = executor.submit(async_task)
            futures.append(future)
        # Wait for all tasks to complete.
        for future in futures:
            future.get()
    end = time.time()
    total_time = end - start
    executor.shutdown()
    executor.awaitTermination(1, TimeUnit.MINUTES)
    return total_time

if __name__ == "__main__":
    runtime = benchmark_async()
    result = {
        "benchmark": "jython_async_benchmark",
        "runtime": runtime,
        "iterations": iterations,
        "timestamp": time.time()
    }
    print(json.dumps(result))
