import sys

input = sys.stdin.readline

pi = 3.1415927
count = 1

while True:
    total = 0
    time = 0
    mph = 0
    a,b,c = input().rstrip().split()
    a = float(a)
    b = int(b)
    c = float(c)
    if b == 0:
        break
    total = a*pi*b
    total /= 12 # 1피트
    total /= 5280 # 1마일
    time = c/3600
    mph = total/time
    total = round(total,2)
    mph = round(mph,2)
    print(f'Trip #{count}: {total:.2f} {mph:.2f}')
    count += 1
