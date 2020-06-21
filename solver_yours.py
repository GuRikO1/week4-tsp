#!/usr/bin/env python3

import sys
import math
import numpy as np

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


def solve(cities):
    N = len(cities)

    # How to structure edge costs
    dist = get_euclidean_distance(cities, N)
    
    # dist_for_solution = dist  # normal

    # dist_for_solution = get_minus_mean_distance(dist, N)  # minus-mean

    dist_for_solution = get_minus_k_mean_distance(dist, N, K)  # minus-k-mean

    # How to construct a first solution
    # solution = nearest_neighbor(dist_for_solution, N)  # nearest_neighbor

    solution = kruskal(dist_for_solution, N)  # kruscal

    # improvement
    solution = opt2(solution, dist, N)  # 2-opt

    # solution, _ = oropt1(solution, dist, N)  # or-1-opt

    # solution, _ = oropt2(solution, dist, N)  # or-2-opt

    is_improved = True
    while is_improved:  # iteraion
        solution, flag2 = oropt2(solution, dist, N)
        solution, flag1 = oropt1(solution, dist, N)
        is_improved = flag1 or flag2

    return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
