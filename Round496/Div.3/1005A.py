import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

starts = [idx for idx, val in enumerate(A) if val==1] + [n]

cnt = len(starts) - 1
ans = []
for i in range(cnt):
    d = starts[i+1] - starts[i]
    ans.append(d)
    
print(cnt)
print(*ans)