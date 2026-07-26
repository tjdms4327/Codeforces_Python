import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    
    upper_idx = []
    lower_idx = []
    for i, x in enumerate(s):
        if x == 'b':
            if lower_idx:
                lower_idx.pop()
        elif x == 'B':
            if upper_idx:
                upper_idx.pop()
        elif x.isupper():
            upper_idx.append(i)
        elif x.islower():
            lower_idx.append(i)
            
    result_idx = sorted(upper_idx + lower_idx)
    if result_idx:
        ans = [s[i] for i in result_idx]
    else:
        ans = ['']
        
    print(''.join(ans))