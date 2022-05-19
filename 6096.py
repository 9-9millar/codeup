d=[]
for i in range(19) : 
    d.append(list(map(int,input().split())))

n = int(input())

for i in range(n):
    x, y = input().split()
    for j in range(19):
        if d[j][int(y)-1] == 1:
            d[j][int(y)-1] = 0
            
        else:
            d[j][int(y)-1] = 1

        if d[int(x)-1][j] == 1:
            d[int(x)-1][j] = 0
        else:   
            d[int(x)-1][j] = 1
for i in range(19):
    for j in range(19):
        print(d[i][j],end=' ')
    print()