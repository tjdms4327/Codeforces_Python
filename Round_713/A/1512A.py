import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    for x in set(nums):
        if nums.count(x) == 1:
            cand = x
            break
    
    print(nums.index(cand)+1)
