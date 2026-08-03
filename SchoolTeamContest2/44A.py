import sys
input = sys.stdin.readline

n = int(input())

leaves = set(input().strip() for _ in range(n))
print(len(leaves))