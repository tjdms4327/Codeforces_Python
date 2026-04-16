# C1. Lost Civilization (Easy Version)


### LIMIT
time limit per test: 2 seconds

memory limit per test: 256 megabytes

### PROBLEM
This is the easy version of the problem. The difference between the versions is that in this version, you must compute a value for one sequence. You can hack only if you solved all versions of this problem.

Let's define an algorithm to generate a sequence of m+k
 integers as follows:

First, receive a sequence x
 of m
 integers as input. If k=0
, terminate immediately and return the sequence x
.
Then, select any index 1≤i≤|x|
 and insert (xi+1)
 immediately after the element xi
.
If x
 contains exactly m+k
 integers, terminate and return the sequence x
. Otherwise, return to the second step.
Alice knows that this algorithm was used by an ancient civilization in order to hide their secrets safely. Alice wants to learn the knowledge that they wanted to hide, but it is not an easy job to infer the input from the output of the algorithm.

Given a sequence a
 of n
 integers, determine the length of the shortest sequence that could be given as an input for the algorithm to generate a
.

### Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤104
). The description of the test cases follows.

The first line of each test case contains a single integer n
 (1≤n≤300000
).

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤109
).

It is guaranteed that the sum of n
 over all test cases does not exceed 300000
.

### Output
For each test case, output the length of the shortest sequence on a separate line.
