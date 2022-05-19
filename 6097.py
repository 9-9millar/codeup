h,w = map(int,input().split())
n = int(input())

list=[]
for i in range(h):
    list.append([])
    for j in range(h):
        list[i].append(int(0))


for _ in range(n):
    l,d,x,y = map(int,input().split())
    x = x - 1
    y = y - 1
    if list[x][y] == 0:
        list[x][y] = 1
    if d == 0:
        for i in range(1,l):
            list[x][y+i] = 1
    if d == 1:
        for i in range(1,l):
          list[x+i][y] = 1
for i in range(h):
    for j in range(w):
        print(list[i][j],end=' ')
    print()
