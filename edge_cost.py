#!/usr/bin/env python3

import sys
import math
import numpy as np


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def get_euclidean_distance(cities, N):
    """
    'normal' noted in README
    """
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    return dist


def get_minus_mean_distance(dist, N):
    """
    'minus-mean' noted in README
    """
    ave_dist = np.mean(dist, axis=1)
    dist = [[dist[i][j] - (ave_dist[i] + ave_dist[j])
            for i in range(N)] for j in range(N)]
    return dist


def get_minus_k_mean_distance(dist, N, k):
    """
    'minus-k-mean' noted in README
    """
    ave_dist = np.mean(np.sort(dist, axis=1)[:, 1:min(N, k + 1)], axis=1)
    dist = [[dist[i][j] - (ave_dist[i] + ave_dist[j])
            for i in range(N)] for j in range(N)]
    return dist
