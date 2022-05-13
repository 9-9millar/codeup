a, b = input().split()
a = int(a)
b = int(b)

print((bool(a) and bool(b)) or (not bool(a) and not bool(b)))