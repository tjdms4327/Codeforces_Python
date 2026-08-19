import sys
input = sys.stdin.readline

n, m = map(int, input().split())

diff = []
tot = 0
for _ in range(n):
    a, b = map(int, input().split())
    diff.append(a-b)
    tot += a    
diff.sort(reverse=True)

i = 0
while tot > m :
    if i >= n:
        print(-1)
        sys.exit()
        
    d = diff[i]
    tot -= d
    i += 1


print(i)