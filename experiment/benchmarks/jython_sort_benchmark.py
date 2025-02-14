#!/usr/bin/env jython
import time
import json
from java.util import Arrays
from java.lang import Integer
import random

def sort_benchmark():
    iterations = 10
    size = 100000  # number of elements in the array
    # Generate a list of random integers
    data = [random.randint(0, 1000000) for _ in range(size)]
    # Convert the Python list into a Java array of Integer objects
    java_array = [Integer(val) for val in data]
    
    total_time = 0.0
    for _ in range(iterations):
        # Make a copy of the array for each iteration
        arr = java_array[:]  
        start = time.time()
        Arrays.sort(arr)  # sort using Java's highly optimized sort
        end = time.time()
        total_time += (end - start)
    return total_time

if __name__ == "__main__":
    runtime = sort_benchmark()
    result = {
        "benchmark": "jython_sort_benchmark",
        "runtime": runtime,
        "iterations": 10,
        "timestamp": time.time()
    }
    print(json.dumps(result))
