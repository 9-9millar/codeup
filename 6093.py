n = int(input())    # 10 대입
a = input().split() # 출석 번호
                    # 10 4 2 3 6 6 7 9 8 5

for i in range(n-1,-1,-1):
    print(a[i], end=' ') # 10 4 2 3 6 6 7 9 8 5 가 정수가 됨
