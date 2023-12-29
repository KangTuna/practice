import sys

input = sys.stdin.readline

K,N = map(int,input().rstrip().split())
lan_data = []
for _ in range(K):
    lan_data.append(int(input().rstrip()))

start = 1
end = max(lan_data)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in lan_data:
        count += i//mid
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)