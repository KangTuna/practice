matrix = []
for i in range(9):
    N = list(map(int,input().split()))
    matrix.append(N)
max = 0
col = 0
row = 0
for i in range(9):
    for j in range(9):
        if matrix[i][j] > max:
            max = matrix[i][j] 
            col = i
            row = j

print(max)
print(col+1,row+1)
