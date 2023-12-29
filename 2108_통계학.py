import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))
#산술평균
avg = int(round(sum(arr)/len(arr),0))

#중간값
arr.sort()
midian = arr[int(len(arr)/2)]

#최빈값
cnt = Counter(arr).most_common()
if len(cnt) == 1:
    mode = cnt[0][0]
else:
    if cnt[0][1] == cnt[1][1]:
        mode = cnt[1][0]
    else:
        mode = cnt[0][0]

#범위
scale = max(arr) - min(arr)

print(avg)
print(midian)
print(mode)
print(scale)


