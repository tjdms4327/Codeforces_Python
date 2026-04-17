# B. Flipping Binary String


### LIMIT
time limit per test: 1.5 seconds

memory limit per test: 256 megabytes


### PROBLEM
You are given a binary string s
 of length n
. You can perform the following operation on the string:

Choose an index i
, and flip the bit present at all other indices except for the index i
. In other words, choose an integer i
 (1≤i≤n
), and for all j
 such that 1≤j≤n
 and j≠i
, if sj=0
, then set sj:=1
, otherwise set sj:=0
.
You can perform the operation any number of times, but each index can be chosen by at most one operation.

Your task is to make all bits present in the string s
 equal 0
, or report that it is impossible to do so. You don't have to minimize the number of operations.

### Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤104
). The description of the test cases follows.

The first line of each test case contains a single integer n
 (1≤n≤2⋅105
).

The second line of each test case contains the binary string s
 of length n
.

It is guaranteed that the sum of n
 over all test cases does not exceed 2⋅105
.

### Output
For each test case, output −1
 if it is impossible to transform all bits to 0
. Otherwise, output two lines in the following format:

In the first line, print the number of operations x
 (0≤x≤n
).
In the second line of each test case, print x
 numbers – the indices you select in each operation in order. You should guarantee that each index is chosen at most once.
If there are multiple possible solutions, you may output any.
