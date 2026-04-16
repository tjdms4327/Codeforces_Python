import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    if n==1:
        print('NO')
    else:
        stack = []
        for x in s:
            if stack and stack[-1]==x:
                stack.pop()
            else:
                stack.append(x)
        
        if stack:
            print('NO')
        else:
            print('YES')
