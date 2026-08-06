import sys
input = sys.stdin.readline

T = [k*(k+1)//2 for k in range(1, 501)]

n = int(input())
if n in T:
    print('YES')
else:
    print('NO')
