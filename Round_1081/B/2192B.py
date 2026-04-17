import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input().strip())
    
    one =  s.count('1')
    zero = n - one
    
    if one % 2 == 0:
        result = [i+1 for i in range(n) if s[i] == '1']
    elif zero % 2 == 1:
        result = [i+1 for i in range(n) if s[i] == '0']
    else:
        print(-1)
        continue
    
    print(len(result))
    if result:
        print(*result)
