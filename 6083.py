r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)

for i in range(r):
    for k in range(g):
        for s in range(b):
            print(i,k,s)
print(r*g*b)