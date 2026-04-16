A# . Parkour Design


### LIMIT
time limit per test: 1 second

memory limit per test: 256 megabytes


### PROBLEM
Today, Alex wants to build a parkour course for Steve to train his parkour skills on. A parkour course is a sequence p0→p1→…→pk
 of integer coordinates on the plane. Here, a contiguous pair of coordinates is called a move, denoted as pi−1→pi
.

Alex knows that Steve can only perform the following types of moves:

(xi,yi)→(xi+2,yi+1)
;
(xi,yi)→(xi+3,yi)
;
(xi,yi)→(xi+4,yi−1)
.
Note that Steve will not perform any other type of moves. For example, Steve can perform (0,0)→(2,1)
 and (2,1)→(5,1)
, but will never perform moves such as (2,1)→(3,2)
, (3,0)→(5,−1)
, or (4,−1)→(6,−1)
 (even though they may look very easy).

You are given an integer coordinate (x,y)
 on the plane.

Please determine if it is possible to make a parkour course q0,q1,…,qk
 that satisfies the following conditions:

q0=(0,0)
;
qk=(x,y)
;
The parkour course only consists of moves that Steve can perform.

### Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤103
). The description of the test cases follows.

The only line of each test case contains two integers x
 and y
 (1≤x≤109
, −108≤y≤108
).

### Output
If it is possible to make a parkour course that satisfies the conditions, output "YES" on a separate line.

If it is impossible to make a parkour course that satisfies the conditions, output "NO" on a separate line.

You can output the answer in any case. For example, the strings "yEs", "yes", and "Yes" will also be recognized as positive responses.
