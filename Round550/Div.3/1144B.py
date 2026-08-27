import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

even, odd = [], []
for a in A:
    if a%2:
        odd.append(a)
    else:
        even.append(a)
        
len_e, len_o = len(even), len(odd)
if len_e > len_o:
    print(sum(even[len_o+1:]))
else:
    print(sum(odd[len_e+1:]))
