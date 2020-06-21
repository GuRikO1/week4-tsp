#!/usr/bin/env python3

import sys
import math
import numpy as np
import time

from common import print_solution, read_input
from edge_cost import (
    get_euclidean_distance,
    get_minus_mean_distance,
    get_minus_k_mean_distance
)
from nearest_neighbor import nearest_neighbor
from kruskal import kruskal
from opt2 import opt2
from oropt1 import oropt1
from oropt2 import oropt2

K = 10  # minus-k-mean


def get_sum_distance(solution, dist, N):
    ans = 0
    for i in range(N):
        ans += dist[solution[i]][solution[(i + 1) % N]]
    return ans


def solve(argv, cities, N):
    # How to structure edge costs
    dist = get_euclidean_distance(cities, N)
    dist_for_solution = []

    if argv[1] == 'normal':
        dist_for_solution = dist

    elif argv[1] == 'minus-mean':
        dist_for_solution = get_minus_mean_distance(dist, N)

    elif argv[1] == 'minus-k-mean':
        dist_for_solution = get_minus_k_mean_distance(dist, N, K)

    else:
        print('cannot find how to struct edge cost')
        return

    # How to construct a first solution
    if argv[2] == 'nearest_neighbor':
        solution = nearest_neighbor(dist_for_solution, N)

    elif argv[2] == 'kruskal':
        solution = kruskal(dist_for_solution, N)

    else:
        print('cannot find how to construct a first solution')
        return

    # improvement
    if argv[3] == '2-opt':
        solution = opt2(solution, dist, N)

    elif argv[3] == '2-opt+or-1-opt':
        solution = opt2(solution, dist, N)
        solution, _ = oropt1(solution, dist, N)

    elif argv[3] == '2-opt+or-2-opt':
        solution = opt2(solution, dist, N)
        solution, _ = oropt2(solution, dist, N)

    elif argv[3] == '2-opt+iter':
        solution = opt2(solution, dist, N)
        is_improved = True
        while is_improved:  # iteraion
            solution, flag2 = oropt2(solution, dist, N)
            solution, flag1 = oropt1(solution, dist, N)
            is_improved = flag1 or flag2

    elif argv[3] != 'none':
        print('cannot find how to improve solution')
        return

    return solution, dist


if __name__ == '__main__':
    assert len(sys.argv) == 4
    print(sys.argv[1], sys.argv[2], sys.argv[3])
    for i in range(7):
        cities = read_input('input_{}.csv'.format(i))
        start = time.time()
        N = len(cities)
        solution, dist = solve(sys.argv, cities, N)
        elapsed_time = time.time() - start
        sum_distance = get_sum_distance(solution, dist, N)
        print('CHALLENGE {}'.format(i))
        print('sum_distance =', sum_distance)
        print('time = {}[s]\n'.format(elapsed_time))
