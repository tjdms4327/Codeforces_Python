import sys
input = sys.stdin.readline

n = int(input())
D = list(map(int, input().split()))
a, b = map(int, input().split())

prefix = [0]*n
for i in range(1, n):
    prefix[i] = prefix[i-1] + D[i-1]

print(prefix[b-1] - prefix[a-1])