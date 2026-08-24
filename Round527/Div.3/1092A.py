import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    
    s = [chr(ord('a')+i) for i in range(k)] * (n//k + 1)
    ans = ''.join(s[:n])
    
    print(ans)