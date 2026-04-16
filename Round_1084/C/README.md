# C. Specialty String


### LIMIT
time limit per test: 2 seconds

memory limit per test: 256 megabytes


### PROBLEM
AksLolCoding is playing a game on a string s
 of length n
. Initially, s
 contains only lowercase Latin characters.

In one turn, AksLolCoding can choose any pair of integers (i,j)
 such that:

1≤i<j≤n
;
si=sj≠∗
; and
sk=∗
 for all i<k<j
.
If no such i,j
 exists, then the game ends. Otherwise, AksLolCoding sets si:=∗
 and sj:=∗
.
Once the game ends, AksLolCoding wins if and only if every character in s
 is equal to ∗
. Determine if it is possible for AksLolCoding to win.

Note: ∗
 represents ASCII character 42.

### Input
The first line contains an integer t
 (1≤t≤100
), the number of test cases.

The first line of each test case contains an integer n
 (1≤n≤5000
), the length of the string.

The second line of each test case contains a string s
 consisting of lowercase Latin characters.

The sum of n
 over all test cases does not exceed 5000
.

### Output
Output the answer to each test case on its own line. If AksLolCoding can win, output "YES" (without quotes). Else, output "NO" (without quotes).

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
