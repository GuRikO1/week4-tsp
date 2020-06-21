#!/usr/bin/env python3

import sys
import math
import numpy as np


def oropt2(solution, dist, N):
    is_improved = False
    while True:
        count = 0
        for i in range(N):
            i0 = i
            i1 = (i + 1) % N
            i2 = (i + 2) % N
            i3 = (i + 3) % N
            for j in range(N):
                j0 = j
                j1 = (j + 1) % N
                if j0 not in {i0, i1, i2}:
                    l1 = dist[solution[i0]][solution[i1]]
                    l2 = dist[solution[i2]][solution[i3]]
                    l3 = dist[solution[j0]][solution[j1]]
                    l4 = dist[solution[j0]][solution[i1]]
                    l5 = dist[solution[j1]][solution[i2]]
                    l6 = dist[solution[i0]][solution[i3]]
                    if l1 + l2 + l3 > l4 + l5 + l6:
                        if i2 == 0:
                            city1 = solution.pop(i1)
                            city2 = solution.pop(i2)
                            solution.insert(j0, city2)
                            solution.insert(j0, city1)
                        else:
                            city2 = solution.pop(i2)
                            city1 = solution.pop(i1)
                            if i1 < j1:
                                solution.insert(j0 - 1, city2)
                                solution.insert(j0 - 1, city1)
                            else:
                                solution.insert(j1, city2)
                                solution.insert(j1, city1)
                        count += 1
        if count == 0:
            break
        else:
            is_improved = True

    return solution, is_improved
