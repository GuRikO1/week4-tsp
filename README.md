## Build@Mercari 2020 Week4 - Travelling Salesman PRoblem Challenges.

----
## Descripition
My TSP solver algorithm can be divided into three main parts.

1. How to structure edge costs
2. How to construct a first solution
3. Improvement

Each part is described in the followings.

1. How to structure edge costs
    - ***normal***: normal Euclidean diatance

        The distance between the two nodes is the Euclidean distance derived from the coordinates.

    - ***minus-mean***: normal - the distance average of both end nodes (reference[1])

        It takes into account the distribution of the cost of edges leaving a node. If the distance average of both end nodes is large, we need to choose the edges with priority for preventing from getting local opitimal solution.

    - ***minus-k-means***: normal - the distance average (k minimum edges) of both end nodes  

        As we improve the solution, we only need to consider the average of the k edges, in decreasing order, since no edges grow between nodes at too great a distance.
    
2. How to construct a first solution
    - nearest-neighbor:

        It chooses the point in a given set that is closest (or most similar) to a given point.

    - [kruskal](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm): 

        A [minimum-spanning-tree](https://en.wikipedia.org/wiki/Minimum_spanning_tree#Algorithms) algorithm which finds an edge of the least possible weight that connects any two trees in the forest.

3. Improvement 

    - 2-opt:

        ```
        - A   B -             - A - B -
            ×         ==>
        - C   D -             - C - D -
        ```

    - or-1-opt:

        ```
        - A       C -             - A   -   C -
            \   /     
              B           ==>           B
                                      /   \
        - D   -   E -             - D       E -
        ``` 

    - or-2-opt:

        ```
        - A           D -             - A     -     D -
            \       /                     
              B - C           ==>           B - C
                                          /       \
        - D     -     E -             - D           E -
        ``` 

    - iter: iterative processing (or-1-opt + or-2-opt) while being improved

## Usage (Additional)
You can try all algorithm explained in description at hand.
Background operarion is recommended.
```
sh results.sh > results.txt
```

## Evaluation

CPU: 2.6 GHz 6-Core Intel Core i7

|                                        | N = 5   | N = 8   | N = 16  | N = 64   | N = 128  | N = 512  | N = 2048 | time[s] (N = 2048) |
| ----                                   | ----    | ----    | ----    | ----     | ----     | ----     | ----     | ----               |
| normal + nn                            | 3418.10 | 3832.29 | 5449.44 | 10519.16 | 12684.06 | 25331.84 | 49892.05 | 3.54               |
| normal + nn + 2-opt                    | 3418.10 | 3832.29 | 4994.89 | 8970.05  | 11489.79 | 21363.60 | 42712.37 | 13.79              |
| normal + nn + 2-opt + or-1-opt         | 3291.62 | 3778.72 | 4494.42 | 8656.07  | 11225.87 | 20902.75 | 41638.84 | 32.36              |
| normal + nn + 2-opt + or-2-opt         | 3291.62 | 3832.29 | 4816.14 | 8776.23  | 11349.62 | 21189.02 | 42448.43 | 32.85              |
| normal + nn + 2-opt + iter             | 3291.62 | 3778.72 | 4494.42 | 8368.18  | 11069.27 | 20627.84 | 41553.94 | 79.87              |
| normal + kruskal                       | 3518.53 | 3942.55 | 5030.98 | 10459.71 | 12169.94 | 24016.19 | 46470.69 | 13.72              |
| normal + kruskal + 2-opt + iter        | 3291.62 | 3778.72 | 4494.42 | 8398.20  | 10909.24 | 20912.10 | 41006.20 | 103.38             |
| minus-mean + nn                        | 3291.62 | 4199.31 | 5188.88 | 9214.46  | 11794.32 | 23538.46 | 47005.96 | 6.24               | 
| minus-mean + nn + 2-opt + iter         | 3291.62 | 3778.72 | 4494.42 | 8355.93  | 11047.07 | 21149.53 | 41998.41 | 79.13              |
| minus-mean + kruskal                   | 3520.67 | 3778.72 | 4664.52 | 8578.37  | 11183.61 | 22050.37 | 43029.48 | 17.84              |
| minus-mean + kruskal + 2-opt + iter    | 3291.62 | 3778.72 | 4494.42 | 8355.93  | 10702.32 | 20789.26 | 40976.88 | 86.86              |
| minus-10-mean + nn                     | 3291.62 | 4199.31 | 5011.40 | 10101.06 | 13304.56 | 24729.46 | 50002.37 | 6.39               |
| minus-10-mean + nn + 2-opt + iter      | 3291.62 | 3778.72 | 4494.42 | 8465.40  | 11338.02 | 21162.79 | 41181.11 | 66.64              |
| minus-10-mean + kruskal                | 3291.62 | 3778.72 | 4977.70 | 8398.26  | 13139.46 | 21892.52 | 44052.85 | 17.30              |
| ***minus-10-mean + kruskal + 2-opt + iter*** | 3291.62 | 3778.72 | 4494.42 | 8118.40  | 10549.04 | 20418.74 | 40659.50 | 71.82              |


## Reference
1. [巡回セールスマン問題の近似アルゴリズムについて](https://mie-u.repo.nii.ac.jp/?action=repository_action_common_download&item_id=5071&item_no=1&attribute_id=17&file_no=1)
2. [巡回セールスマン問題[3]](http://www.nct9.ne.jp/m_hiroi/light/pyalgo64.html)

----
----

This is forked from [https://github.com/hayatoito/google-step-tsp-2016](https://github.com/hayatoito/google-step-tsp-2016).

1. 問題
[巡回セールスマン問題](https://ja.wikipedia.org/wiki/%E5%B7%A1%E5%9B%9E%E3%82%BB%E3%83%BC%E3%83%AB%E3%82%B9%E3%83%9E%E3%83%B3%E5%95%8F%E9%A1%8C) を解くアルゴリズムを考えてください。

2. 課題
----
このrepositoryを自分のgithubにforkして使ってください。
N = 5 から N = 2048までの７つの課題があります。

| Challenge    | N (= the number of cities) | Input file  | Output (Solution) file |
| ------------ | -------------------------: | ----------- | ---------------------- |
| Challenge 0  |                          5 | input_0.csv | solution_yours_0.csv   |
| Challenge 1  |                          8 | input_1.csv | solution_yours_1.csv   |
| Challenge 2  |                         16 | input_2.csv | solution_yours_2.csv   |
| Challenge 3  |                         64 | input_3.csv | solution_yours_3.csv   |
| Challenge 4  |                        128 | input_4.csv | solution_yours_4.csv   |
| Challenge 5  |                        512 | input_5.csv | solution_yours_5.csv   |
| Challenge 6  |                       2048 | input_6.csv | solution_yours_6.csv   |

inputとoutputの形式については *3. Data Format Specification* を見てください。
### Your tasks

* 巡回セールスマン問題をとくアルゴリズムを考えて実装してください。
* `solution_yours_{0-6}.csv` をあなたのアルゴリズムでといた結果で上書きしてください。
* あなたの解法の*path length*を[scoreboard]に書いてください

[scoreboard]: https://docs.google.com/spreadsheets/d/1t4ScULZ7aZpDJL8i9AVFQfqL7sErjT5i3cmC1G5ecR8/edit?usp=sharing
### An optional task (Speed challenge)

What matters in this optional task is your program's *speed* (execution time). The path length does not matter as long as it meets the condition.
Your task is:

* Given `input_6.csv`, write a program which outputs a path shorter than `47,000`

Input your program's execution time in the [scoreboard]. Faster (smaller) is better.

You can measure the execution time by `time` command.

```shellsession
$ time yourprogram input_6.csv solution_yours_6.csv
2.96s user 0.07s system 97% cpu 3.116 total
```

In this case, your score is `3.116` (s).

### Visualizer

The demo page of the visualizer is:
https://mercari-build.github.io/week4-tsp/visualizer/.

The assignment includes a helper Web page, `visualizer/index.html`, which
visualizes your solutions. You need to run a HTTP server on your local machine
to access the visualizer. Any HTTP server is okay. If you are not sure how to
run a web server, use the following command to run the HTTP server included in
the assignment. Make sure that you are in the top directory of the assignment
before running the command.

``` shellsession
./nocache_server.py # For Python 3
./nocache_server.py2.py # If you don’t want to install Python3
```

Then, open a browser and navigate to the
[http://localhost:8000/visualizer/](http://localhost:8000/visualizer/). Note
that visualizer was only tested by Google Chrome.  Using the visualizer is
up-to you. You don’t have to use the visualizer to finish the assignment. The
visualizer is provided for the purpose of helping you understand the problem.

3. Data Format Specification
----

### Input Format

The input consists of `N + 1` lines. The first line is always `x,y`. It is followed by `N` lines, each line represents an i-th city’s location, point `xi,yi` where `xi`, `yi` is a floating point number.

```
x,y
x_0,y_0
x_1,y_1
…
x_N-1,y_N-1
```

### Output Format

Output has `N + 1` lines. The first line should be “index”. It is followed by `N` lines, each line is the index of city, which represents the visitation order.

```
index
v_0
v_1
v_2
…
v_N-1
```

### Example (Challenge 0, N = 5)

Input Example:

```
x,y
214.98279057984195,762.6903632435094
1222.0393903625825,229.56212316547953
792.6961393471055,404.5419583098643
1042.5487563564207,709.8510160219619
150.17533883877582,25.512728869805677
```

Output (Solution) Example:

```
index
0
2
3
1
4
```

These formats are requirements for the visualizer, which can take only properly formatted CSV files as input.

5. What’s included in the assignment
----

To help you understand the problem, there are some sample scripts / resources
in the assignment, including, but not limited to:

- `solver_random.py` - Sample stupid solver. You never lose to this stupid one.
- `solution_random_{0-6}.csv` - Sample solutions by solver_random.py.
- `solver_greedy.py` - Sample solver using the greedy algorithm. You should beat this definitely.
- `solution_greedy_{0-6}.csv` - Sample solutions by solver_greedy.py.
- `solution_sa_{0-6}.csv` - Yet another sample solutions. I expect all of you will beat this one too. The solver itself is not included intentionally.
- `solution_wakanapo_{0-6}.csv` - Sample solutions I solved when I was joined Google STEP 2016.
- `solution_yours_{0-6}.csv` - You should overwrite these files with your solution.
- `solution_verifier.py` - Try to validate your solution and print the path length.
- `input_generator.py` - Python script which was used to create input files, `input_{0-6}.csv`
- `visualizer/` - The directory for visualizer.

6. Acknowledgments
----
この課題は[私](https://github.com/wakanapo)がgoogle step 2016に参加したときにやったものです。問題のわかりやすさ、visualizerによるアルゴリズムのみやすさ、楽しさなどにおいてこれを上回る課題はないと思ったので、Build@Mercariでも採用することにしました。

----
