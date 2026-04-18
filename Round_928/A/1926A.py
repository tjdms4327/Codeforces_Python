import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    
    cnt_A = s.count('A')
    if cnt_A > 2:
        print('A')
    else:
        print('B')
