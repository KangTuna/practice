T = int(input())
for i in range(T):
    k = int(input()) + 1# 층수
    n = int(input()) # 호수
    data = [[0 for i in range(n)]for i in range(k)]
    for j in range(n):
        data[0][j] = j+1
    for j in range(k):
        data[j][0] = 1
    for z in range(1,k):
        for j in range(1,n):
            data[z][j] = data[z-1][j] + data[z][j-1]
    print(data[k-1][n-1])

        
