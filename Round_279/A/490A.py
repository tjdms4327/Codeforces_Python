import sys
input = sys.stdin.readline

n = int(input())
T = list(map(int, input().split()))

ti = {1:[], 2:[], 3:[]}
for idx, x in enumerate(T, start=1):
    ti[x].append(idx)
    
Min = min(len(val) for val in ti.values())
print(Min)
for i in range(Min):
    print(ti[1][i], ti[2][i], ti[3][i])
