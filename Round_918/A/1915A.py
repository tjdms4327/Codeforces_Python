import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    nums.sort()
    
    if nums[0]==nums[1]:
        print(nums[2])
    elif nums[0]==nums[2]:
        print(nums[1])
    else:
        print(nums[0])
