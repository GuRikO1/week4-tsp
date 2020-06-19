#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input
from solver_nearest_neighbor import get_all_distance, nearest_neighbor


def two_opt(solution, dist, N):
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


def solve(cities):
    N = len(cities)
    dist = get_all_distance(cities, N)
    solution = nearest_neighbor(dist, N)
    solution = two_opt(solution, dist, N)
    return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
