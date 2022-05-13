n = int(input())
for i in range(1,n+1):
    r = i % 10
    if i % 10 == 0:
        print(i, end=' ')
    elif r % 3 == 0:
        print('X', end=' ')
    else:
        print(i, end=' ')
        