# A. Polycarp and Coins


### LIMIT
time limit per test: 1 second

memory limit per test: 256 megabytes


### PROBLEM
Polycarp must pay exactly n
 burles at the checkout. He has coins of two nominal values: 1
 burle and 2
 burles. Polycarp likes both kinds of coins equally. So he doesn't want to pay with more coins of one type than with the other.

Thus, Polycarp wants to minimize the difference between the count of coins of 1
 burle and 2
 burles being used. Help him by determining two non-negative integer values c1
 and c2
 which are the number of coins of 1
 burle and 2
 burles, respectively, so that the total value of that number of coins is exactly n
 (i. e. c1+2⋅c2=n
), and the absolute value of the difference between c1
 and c2
 is as little as possible (i. e. you must minimize |c1−c2|
).

### Input
The first line contains one integer t
 (1≤t≤104
) — the number of test cases. Then t
 test cases follow.

Each test case consists of one line. This line contains one integer n
 (1≤n≤109
) — the number of burles to be paid by Polycarp.

### Output
For each test case, output a separate line containing two integers c1
 and c2
 (c1,c2≥0
) separated by a space where c1
 is the number of coins of 1
 burle and c2
 is the number of coins of 2
 burles. If there are multiple optimal solutions, print any one.
