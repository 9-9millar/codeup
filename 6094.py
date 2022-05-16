n = int(input())
a = input().split() #10 4 2 3 6 6 7 9 8 5 

for i in range(n):
    a[i] = int(a[i])
    
print(min(a))