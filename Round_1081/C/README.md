# C. All-in-one Gun


### LIMIT
time limit per test: 2 seconds

memory limit per test: 256 megabytes


### PROBLEM
You are developing a new shooter game, but since there are a lot of shooter games out there, you decide to have something unique in your game.

You have an all-in-one gun that shoots bullets in a fixed order. There are n
 bullets in the magazine, the i
-th of which deals ai
 damage. The enemy starts with h
 health and dies when its health becomes ≤0
.

The gun shoots one bullet per second. After firing all n
 bullets, it must reload, which takes k
 seconds. Reloading always restores the same sequence of bullets [a1,a2,…,an]
. You cannot reload early; you must empty the magazine first. At the start, the magazine is already full.

Before the fight begins, you may perform at most one swap: pick any indices 1≤i<j≤n
 and exchange ai
 with aj
.

Your task is to find the minimum number of seconds needed to kill the enemy, taking into account this optional single swap.

### Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤104
). The description of the test cases follows.

The first line of each testcase contains three integer n
, h
 and k
 (2≤n≤2⋅105
, 1≤h,k≤109
) — the size of magazine, health of your enemy and time required to reload the magazine.

The second line of each testcase contains n
 integers a1,a2,…,an
 (1≤ai≤109
).

It is guaranteed that the sum of n
 does not exceed 2⋅105
 over all test cases.

### Output
For each testcase, output a single integer denoting the minimum time required to kill the enemy.
