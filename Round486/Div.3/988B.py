import sys
input = sys.stdin.readline

n = int(input())
strings = [input().strip() for _ in range(n)]

strings.sort(key = lambda x:len(x))


for i in range(1, n):
    if strings[i-1] not in strings[i]:
        print('NO')
        break
else:
    print('YES')
    print(*strings, sep='\n')