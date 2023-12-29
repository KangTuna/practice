import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

def search(x,y,n):
  global w,b,c
  c += 1
  t = field[x][y]
  for i in range(x,x+n):
    for j in range(y,y+n):
      if field[i][j] != t:
        m = n//2
        for a in range(2):
          for c in range(2):
            #print(x+m*a,y+m*b,m,field[x+m*a][y+m*b])
            search(x+m*a,y+m*c,m)
        return
  #print(t)
  if t == 1:
    b += 1
  elif t == 0:
    w += 1
  #print(w,b)
n = int(input().rstrip())
field = [list(map(int,input().rstrip().split())) for _ in range(n)]
global w,b,c
w,b,c = 0,0,0
# print(w,b)
search(0,0,n)
print(w,b,sep="\n")