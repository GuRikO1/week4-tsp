#!/usr/bin/env python3

import math
import sys
import random

from common import print_solution, read_input

random.seed(1)


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def random_solution(N):
    solution = list(range(N))
    random.shuffle(solution)
    return solution


def solve(cities):
    N = len(cities)
    solution = random_solution(N)
    return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
