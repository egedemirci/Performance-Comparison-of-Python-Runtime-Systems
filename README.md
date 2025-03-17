# Performance-Comparison-of-Python-Runtime-Systems
This repository is codebase for Runtime Systems project. We implement and evaluate runtime and memory metrics for various benchmarks across three python interpreters - CPython3, PyPy3 and Jython. 

## Set Up
To setup and replicate our benchmark data, installing the same version of interpreters is necessary. To install, run

''' github clone link_to_the_repository
cd path_to_repository
chmod x+w setup.sh
./setup.sh
'''

## Recording runtime for benchmarks
All the benchmarks are located in experiment/benchmarks directory. To run all the benchmarks and record runtime, run

'''
python3 run_experiments.py
'''

This would automatically run all benchmarks across all interpreters and store the runtimes in results.csv in the main directory.

## Memory Profiler Set Up
We use memory_profiler which is the standard python memory profiling tool to collect memory usage statistics. Memory profiler has to be installed individually for each interpreters as follows:
'''
python3 -m pip install memory_profiler
pypy3 -m pip install memory_profiler
jython -m pip install memory_profiler
'''

## Memory Profiling
For each benchmark, run
'''
python3 -m mprof run benchmark.py
mprof plot
'''

This would produce a matplot with graph showing memory usage against runtime. Note: Plotting the graph requires matplotlib package.s