import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = input().strip()
    
    best = 0
    zero = 0
    for c in n:
        if c == '0':
            zero += 1
        else:
            best = max(best, zero+1) # 남길 길이
            
    print(len(n) - best)
            