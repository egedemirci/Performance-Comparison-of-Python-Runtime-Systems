#!/usr/bin/env python3
import timeit
import json
import time
import math
def nbody_simulation(bodies, dt, steps):
    for _ in range(steps):
        for i in range(len(bodies)):
            fx=0.0
            fy=0.0
            for j in range(len(bodies)):
                if i==j:
                    continue
                dx=bodies[j][0]-bodies[i][0]
                dy=bodies[j][1]-bodies[i][1]
                dist=math.sqrt(dx*dx+dy*dy)+1e-10
                force=dt/(dist*dist)
                fx+=force*dx/dist
                fy+=force*dy/dist
            bodies[i][0]+=fx
            bodies[i][1]+=fy
    return bodies
def benchmark_nbody():
    iterations=10
    num_bodies=100
    steps=10
    bodies=[[1.0,2.0] for _ in range(num_bodies)]
    total_time=timeit.timeit(lambda: nbody_simulation(bodies,0.01,steps), number=iterations)
    return total_time
if __name__=="__main__":
    runtime=benchmark_nbody()
    result={"benchmark": "nbody_benchmark", "runtime": runtime, "iterations": 10, "timestamp": time.time()}
    print(json.dumps(result))
