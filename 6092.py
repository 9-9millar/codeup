n = int(input()) #출석 부른 횟수
a = input().split() # 1 3 2 2 5 6 7 4 5 9 

for i in range(n):
    a[i] = int(a[i]) # 정수가 된 1 3 2 2 5 6 7 4 5 9

d = []
for i in range(24):
    d.append(0) # d = [0,0,0,0,...,0] 24개의 0 리스트

for i in range(n):
    d[a[i]] += 1 # a[i]는 학생의 번호 d[i]는 번호 당 불린 횟수
for i in range(1,24):
    print(d[i], end=' ')
    