a = input()
aspace = a.find(' ')
if aspace:
    b = a[:aspace+1]
    c = a[aspace+1:]
    print(b)
    print(c)