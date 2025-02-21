#!/usr/bin/env python3
import subprocess
import json
import csv
import datetime
import time
import resource 

benchmarks = [
    "benchmarks/fib_benchmark.py",
    "benchmarks/sort_benchmark.py",
    "benchmarks/io_benchmark.py",
    "benchmarks/memory_benchmark.py",
    "benchmarks/concurrency_benchmark.py",
    "benchmarks/json_benchmark.py",
    "benchmarks/nbody_benchmark.py",
    "benchmarks/asyncio_benchmark.py",
     "benchmarks/dictionary_benchmark.py" 
]

interpreters = {"CPython": "python3", "PyPy": "pypy3", "Jython": "jython"}
results_csv = "results.csv"

jython_substitutions = {
    "benchmarks/asyncio_benchmark.py": "benchmarks/jython_async_benchmark.py",
    "benchmarks/sort_benchmark.py": "benchmarks/jython_sort_benchmark.py",       # Example substitution
    "benchmarks/dictionary_benchmark.py": "benchmarks/jython_dictionary_benchmark.py"  # Add if available
}

def run_benchmark(interpreter, script):
    start_time = time.time()
    start_cpu = time.process_time()
    rusage_before = resource.getrusage(resource.RUSAGE_CHILDREN)
    
    cmd = [interpreter, script]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, universal_newlines=True)
        data = json.loads(output.strip())
    except subprocess.CalledProcessError as e:
        print(f"Error running {cmd}: {e.output}")
        return None

    end_time = time.time()
    end_cpu = time.process_time()
    rusage_after = resource.getrusage(resource.RUSAGE_CHILDREN)
    
    data["wall_time"] = end_time - start_time
    data["cpu_time"] = end_cpu - start_cpu
    mem_before = rusage_before.ru_maxrss
    mem_after = rusage_after.ru_maxrss
    peak = max(mem_before, mem_after)
    data["peak_memory_MB"] = peak / 1024.0
    data["interpreter"] = interpreter
    data["script"] = script
    if "timestamp" not in data:
        data["timestamp"] = time.time()
    return data

def main():
    all_results = []
    for interp_name, interp_cmd in interpreters.items():
        for bench in benchmarks:
            if interp_name == "Jython" and bench in jython_substitutions:
                substituted = jython_substitutions[bench]
                print(f"Substituting {bench} with {substituted} for Jython.")
                bench = substituted
            print(f"Running {bench} with {interp_name} ({interp_cmd})...")
            result = run_benchmark(interp_cmd, bench)
            if result:
                all_results.append(result)
    if all_results:
        with open(results_csv, "w", newline="") as csvfile:
            fieldnames = [
                "timestamp", "interpreter", "script", "benchmark",
                "iterations", "runtime", "wall_time", "cpu_time", "peak_memory_MB"
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for r in all_results:
                ts = datetime.datetime.fromtimestamp(r.get("timestamp", time.time())).isoformat()
                writer.writerow({
                    "timestamp": ts,
                    "interpreter": r.get("interpreter"),
                    "script": r.get("script"),
                    "benchmark": r.get("benchmark"),
                    "iterations": r.get("iterations"),
                    "runtime": r.get("runtime"),
                    "wall_time": r.get("wall_time"),
                    "cpu_time": r.get("cpu_time"),
                    "peak_memory_MB": r.get("peak_memory_MB")
                })
        print(f"All results have been saved to {results_csv}")
    else:
        print("No results were collected.")

if __name__ == "__main__":
    main()
