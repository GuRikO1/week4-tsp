#!/bin/sh

for argv1 in normal minus-mean minus-k-mean
do
    for argv2 in nearest_neighbor kruskal
    do
        for argv3 in none 2-opt 2-opt+or-1-opt 2-opt+or-2-opt 2-opt+iter
        do
            python3 solver_yours_show.py $argv1 $argv2 $argv3
        done
    done
done