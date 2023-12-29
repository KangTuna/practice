import sys

input = sys.stdin.readline

ga,se,area = map(int,input().rstrip().split())
ans_ga = 0
ans_se = 0
if ga % area == 0:
    ans_ga = ga//area
else:
    ans_ga = (ga//area) + 1

if se % area == 0:
    ans_se = se//area
else:
    ans_se = (se//area) + 1

print(ans_ga * ans_se)