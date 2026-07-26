import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, s, m = map(int, input().split())
    
    schedules = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)] + [(m, m)] 
    
    for i in range(n+1):
        r = schedules[i][1]
        l = schedules[i+1][0]
        
        if l-r >= s:
            print('YES')
            break
        
    else:
        print('NO')