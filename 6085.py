w,h,b = input().split()
w = int(w)
h = int(h)
b = int(b)
data = w*h*b/8/1024/1024
data = float(data)
print(format(data,".2f"),'MB')