# A. Eating Game


### LIMIT
time limit per test: 1 second

memory limit per test: 256 megabytes


### PROBLEM
There are n
 players playing a game at a circular table. The i
-th player has ai
 dishes to eat. They take turns eating the food, and any player can go first.

During their turn, if player i
 has any dishes remaining, they must eat exactly one dish. Then, player (imodn)+1
 starts their turn. This continues until all dishes are finished.

The player who eats the last dish is considered the winner. Determine the number of players that can possibly be winners.

### Input
The first line contains an integer t
 (1≤t≤5000
), the number of test cases.

The first line of each test case contains an integer n
 (1≤n≤10
).

The second line of each test case contains n
 integers, the elements of a
 (1≤ai≤10
).

### Output
For each test case, output a line with the answer.
