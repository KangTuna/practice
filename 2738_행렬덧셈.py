import sys

def arr_plus(arr,arr2):
    temp = arr
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            temp[i][j] = arr[i][j] + arr2[i][j]
    return temp

N,M = map(int,sys.stdin.readline().rstrip().split())

arr = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
arr2 = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]

ans = arr_plus(arr,arr2)

for i in range(len(ans)):
    for j in ans[i]:
        print(j,end=" ")
    print()

