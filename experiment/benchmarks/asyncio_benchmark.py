#!/usr/bin/env python3
import asyncio
import time
import json
def async_task():
    return asyncio.sleep(0.001)
async def run_tasks(n):
    tasks=[async_task() for _ in range(n)]
    await asyncio.gather(*tasks)
async def run_benchmark(n):
    await run_tasks(n)
def benchmark_asyncio():
    iterations=10
    n_tasks=1000
    total_time=0.0
    for _ in range(iterations):
        start=time.time()
        asyncio.run(run_benchmark(n_tasks))
        total_time+=time.time()-start
    return total_time
if __name__=="__main__":
    runtime=benchmark_asyncio()
    result={"benchmark":"asyncio_benchmark","runtime":runtime,"iterations":10,"timestamp":time.time()}
    print(json.dumps(result))
