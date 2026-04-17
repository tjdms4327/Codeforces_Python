import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    if (n//2) % 2 != 0:
        print('NO')
    else:
        print('YES')
        
        left, right = [], []
        for i in range(1, n+1):
            if i % 2 == 0:
                left.append(i)
            else:
                right.append(i)
        right.pop()
        right.append(sum(left) - sum(right))
        
        print(*(left+right))
