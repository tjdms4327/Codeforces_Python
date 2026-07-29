import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a1, a2, a4, a5 = map(int, input().split())
    
    a3 = [a1 + a2, a5-a4]
    
    cnt = 0
    for x in a3:
        cnt = max(cnt, (a1+a2==x) + (a2+x==a4) + (x+a4==a5))
        
        
    print(cnt)