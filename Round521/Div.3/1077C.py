import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(A)
maxes = [sorted_A[-2] if a==sorted_A[-1] else sorted_A[-1] for a in A]

Sum = sum(A)

nice_idx = []
for i in range(n):
    Max = maxes[i]
    
    if Sum - A[i] == 2*Max:
        nice_idx.append(i+1) # 1-based 맞추기
        

m = len(nice_idx)
print(m)
if m:
    print(*nice_idx)