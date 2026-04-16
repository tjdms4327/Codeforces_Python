import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
 
    poss = 'NO'
    for i in range(3):
        for j in range(i+1, 3):
            if nums[i]+nums[j] >= 10:
                poss = 'YES'
                break
        if poss == 'YES':
            break
    print(poss)
