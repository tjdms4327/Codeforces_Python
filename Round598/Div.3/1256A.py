import sys
input = sys.stdin.readline

q = int(input())
for _ in range(q):
    a, b, n, s = map(int, input().split())
    
    n_cnt = s // n
    left = s - n * min(a, n_cnt)
    
    if left > b:
        print('NO')
    else:
        print('YES')