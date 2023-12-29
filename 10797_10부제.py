import sys
input = sys.stdin.readline

n = int(input().rstrip())
data= list(map(int,input().rstrip().split()))

print(data.count(n))