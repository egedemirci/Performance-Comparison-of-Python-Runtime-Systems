#!/usr/bin/env python3
import timeit
import json
import time
def benchmark_json():
    iterations=1000
    data={"key": "value", "numbers": list(range(100))}
    def json_task():
        s=json.dumps(data)
        _=json.loads(s)
    total_time=timeit.timeit(json_task, number=iterations)
    return total_time
if __name__=="__main__":
    runtime=benchmark_json()
    result={"benchmark": "json_benchmark", "runtime": runtime, "iterations": 1000, "timestamp": time.time()}
    print(json.dumps(result))
