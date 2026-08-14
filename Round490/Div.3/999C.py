import sys, string
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(input().strip())

if n == k:
    print('')
    sys.exit()

positions = [[] for _ in range(26)]
for i, ch in enumerate(s):
    positions[ord(ch) - ord('a')].append(i)

left = [True]*n
for delete_lst in positions:
    for idx in delete_lst:
        left[idx] = False
        k -= 1
        
        if k == 0:
            break
    if k == 0:
        break
    
ans = ''.join(s[i] for i in range(n) if left[i])
print(ans)