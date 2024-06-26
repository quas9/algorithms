#!/usr/bin/env python3

from math import inf
from dataclasses import dataclass

FILE_NAME = "job_Var6.in"

A = []

with open(FILE_NAME) as f:
    first_numbers = f.readline().split()
    N = int(first_numbers[0])
    start_v = int(first_numbers[2]) - 1
    for _ in range(N):
        line = f.readline()
        A.append([float(x) if x != "*" else -inf for x in line.split()])

S = set()
S.add(start_v)

D = A[start_v].copy()
D[start_v] = inf

P = [start_v] * N

def float_str(f):
    if f == inf:
        return '*'
    
    if f == -inf:
        return '-'
    
    return str(int(f))

def printi(i):
    print(f'{i}')
    print(f'D: {" ".join([float_str(d) for d in D])} ')
    print(f'P: {" ".join([str(p + 1) for p in P])} ')

@dataclass
class VertexWeight:
    w: float
    v: int

printi(1)
for i in range(N - 2):
    max = VertexWeight(w=-inf, v=start_v)
    # finding max
    for j in range(N):
        if j in S:
            continue
        
        if max.w < D[j]:
            max.v = j
            max.w = D[j]

    S.add(max.v)

    for j in range(N):
        if j in S:
            continue
        
        minimum = min(max.w, A[max.v][j])
        if D[j] < minimum:
            D[j] = minimum
            P[j] = max.v

    
    printi(i+2)
