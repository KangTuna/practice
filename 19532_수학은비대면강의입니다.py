import sys

input = sys.stdin.readline

a,b,c,d,e,f = map(int,input().rstrip().split())

x = int((e*c-b*f)/(a*e-b*d))
y = int((d*c-a*f)/(d*b-a*e))

print(x,y)
