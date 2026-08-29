import sys
input = sys.stdin.readline

a = int(input())

while True:
    if sum(map(int, str(a))) % 4 == 0:
        print(a)
        break
    a += 1