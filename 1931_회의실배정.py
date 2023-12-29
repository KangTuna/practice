import sys

input = sys.stdin.readline
# 데이터 받기
N = int(input().rstrip())
data = []
for _ in range(N):
    start,end = map(int,input().rstrip().split())
    data.append((end,start))
# 끝나는 시간으로 정렬하기

def activtySelection(act):
    result = []
    sorted = act.sort()

