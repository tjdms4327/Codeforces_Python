import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, h, k = map(int, input().split())
    A = list(map(int, input().split()))
    
    onetime = sum(A)
    full = (h - 1) // onetime
    time = full * n + full * k
    h -= full * onetime
    
    # suffix 최대값 
    suffix_max = [0]*n
    suffix_max[-1] = A[-1]
    for i in range(n-2, -1, -1):
        suffix_max[i] = max(A[i], suffix_max[i+1])
    
    prefix = 0
    min_in = float('inf')
    for i in range(n):
        prefix += A[i]
        min_in = min(min_in, A[i])
        
        # swap 없이
        if prefix >= h:
            time += i+1
            break
        
        # swap 가능
        if i+1 < n:
            gain = suffix_max[i+1] - min_in
            if prefix + gain >= h:
                time += i+1
                break
    
    print(time)
