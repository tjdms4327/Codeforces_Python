import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    lst = []
    cur = s[0]
    for i in range(1, n):
        if s[i] == cur[-1]:
            cur += s[i]
        else:
            lst.append(cur)
            cur = s[i]
    if cur:
        lst.append(cur)
            
    count = len(lst)
    if lst[0][0] != lst[-1][0] and max(len(x) for x in lst) >= 2:
        count += 1
    print(count)
