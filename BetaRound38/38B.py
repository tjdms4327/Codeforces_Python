import sys
input = sys.stdin.readline

s1 = input().strip()
look = (ord(s1[0])-ord('a')+1 , int(s1[1]))

s2 = input().strip()
knight = (ord(s2[0])-ord('a')+1 , int(s2[1]))



D = [(-2, -1), (-2, 1), (2, -1), (2, 1),
     (-1, -2), (1, -2), (-1, 2), (1, 2)]

cnt = 0
for r in range(1, 9):
    for c in range(1, 9):
        # 이미 있는 칸에 못 놓음
        if (r, c) in [look, knight]:
            continue
        
        # 룩이 공격하면 안됨
        if r == look[0] or c == look[1]:
            continue
        
        # 새 나이트가 공격하면 안됨
        notAttack = True
        for dx, dy in D:
            nr, nc = dx+r, dy+c
            if 1<=nr<=8 and 1<=nc<=8:
                if (nr, nc) in [look, knight]:
                    notAttack = False
                    break
        
        if notAttack:
            cnt += 1
            

print(cnt)
        