l = []
for _ in range(10):
     l.append(list(map(int,input().split())))
a = int(1)
b = int(1)

for _ in range(1000):
    l[a][b] = 9
    if l[a][b+1] == 0:
        l[a][b+1] = 9
        b = b+1
    elif l[a+1][b] == 0:
        l[a+1][b] = 9
        a = a+1
    elif l[a][b+1] == 2:
        l[a][b+1] = 9
        break
    elif l[a+1][b] == 2:
        l[a+1][b] = 9
        break
        

for i in range(10):
    for j in range(10):
        print(l[i][j],end=' ')
    print()