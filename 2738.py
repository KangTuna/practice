import sys

row,col = map(int,sys.stdin.readline().split())

matrix1 = []
matrix2 = []
matrix = []
for i in range(col):
    matrix1.append(list(map(int,input().split())))
for i in range(col):
    matrix2.append(list(map(int,input().split())))
print(matrix1)
print(matrix2)
for i in range(col):
    for j in range(row):
        print(matrix1[i][j] + matrix2[i][j])
    print()
