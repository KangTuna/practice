import sys
arr = []
for i in range(5):
    N = int(sys.stdin.readline().rstrip())
    arr.append(N)
arr.sort()
print(int(sum(arr)/5))
print(arr[2])