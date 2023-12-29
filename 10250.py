T = int(input()) # 시행횟수
for i in range(T):
    H,W,N = map(int,input().split()) # H : 층수 W : 방의 위치 N : 손님 순서
    temp = N
    count = 0
    while True:
        temp -= H
        count += 1
        if temp < 0:
            break
    temp += H
    if temp == 0:
        temp += H
        count -= 1
    hosil = (temp * 100) + count
    print(hosil)
    
