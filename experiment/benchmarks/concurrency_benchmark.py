#!/usr/bin/env python3
import timeit
import json
import time
import threading

def thread_task():
    return sum(range(10000))

def benchmark_concurrency():
    iterations = 10
    thread_count = 4
    
    def run_threads():
        threads = []
        for _ in range(thread_count):
            t = threading.Thread(target=thread_task)
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
    
    total_time = timeit.timeit(run_threads, number=iterations)
    return total_time

if __name__ == "__main__":
    runtime = benchmark_concurrency()
    result = {
        "benchmark": "concurrency_benchmark",
        "runtime": runtime,
        "iterations": 10,
        "timestamp": time.time()
    }
    print(json.dumps(result))
