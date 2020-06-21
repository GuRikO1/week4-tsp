#!/usr/bin/env python3

import sys
import math
import numpy as np


def opt2(solution, dist, N):
    while True:
        count = 0
        for i in range(N - 2):
            for j in range(i + 2, N):
                l1 = dist[solution[i]][solution[i + 1]]
                l2 = dist[solution[j]][solution[(j + 1) % N]]
                l3 = dist[solution[i]][solution[j]]
                l4 = dist[solution[i + 1]][solution[(j + 1) % N]]
                if l1 + l2 > l3 + l4:
                    new_solution = solution[i + 1:j + 1]
                    solution[i + 1:j + 1] = new_solution[::-1]
                    count += 1
        if count == 0:
            break

    return solution
