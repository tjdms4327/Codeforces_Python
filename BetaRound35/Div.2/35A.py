fin = open("input.txt", "r")
fout = open("output.txt", "w")

ball = int(fin.readline())
for _ in range(3):
    a, b = map(int, fin.readline().split())
    
    if ball == a:
        ball = b
    elif ball == b:
        ball = a
        
print(ball, file=fout)

fin.close()
fout.close()