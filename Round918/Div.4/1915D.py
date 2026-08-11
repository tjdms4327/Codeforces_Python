import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    ans = []
    i = 0
    cur = ''

    while i < n:
        cur += s[i]

        if s[i] in 'ae':
            if (i + 2 < n) and (s[i + 1] in 'bcd') and (s[i + 2] in 'bcd'):
                cur += s[i + 1]
                i += 1
                
            # VC가 문자열의 끝이면 CVC
            elif i + 1 < n and i + 2 == n:
                cur += s[i + 1]
                i += 1

            # 음절 완성
            ans.append(cur)
            cur = ''

        i += 1

    print('.'.join(ans))