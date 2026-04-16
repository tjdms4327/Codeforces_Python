import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    wrong_odd = 0
    wrong_even = 0

    n = int(input())
    A = list(map(int, input().split()))
    
    for idx, a in enumerate(A):
        if idx%2 != a%2:
            if idx % 2 == 0:
                wrong_odd += 1
            else:
                wrong_even += 1
                
    if wrong_even == wrong_odd:
        print(wrong_odd)
    else:
        print(-1)
