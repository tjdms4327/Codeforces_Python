import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
A = list(map(int, input().split()))

counter = Counter(A)
cnt = [val for val in counter.values()]

if any(x>2 for x in cnt):
    print('NO')
    sys.exit()
elif any(x>1 for x in cnt):
    lst1 = [key for key in counter.keys()]
    lst2 = [key for key, val in counter.items() if val==2]
else:
    lst1 = A
    lst2 = []
    
lst1.sort()
lst2.sort(reverse=True)

print('YES')
print(len(lst1))
print(*lst1)
print(len(lst2))
print(*lst2)