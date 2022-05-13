h,b,c,s = input().split()
h = float(h)
b = float(b)
c = float(c)
s = float(s)
data = h * b * c * s /8/1024/1024
print(format(data,".1f"),'MB')