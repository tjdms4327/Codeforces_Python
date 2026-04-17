import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    
    codeforces = 'codeforces'
    diff = 0
    for i in range(10):
        if s[i] != codeforces[i]:
            diff += 1
    print(diff)
