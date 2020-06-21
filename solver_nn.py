#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input
from edge_cost import get_euclidean_distance
from nearest_neighbor import nearest_neighbor


def solve(cities):
    N = len(cities)
    dist = get_euclidean_distance(cities, N)
    solution = nearest_neighbor(dist, N)
    return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
