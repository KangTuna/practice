import math,sys

input = sys.stdin.readline

# 입력값 받기
min_num, max_num = map(int,input().rstrip().split())

# max를 넘지 않는 제곱수의 리스트를 구함
squares = [i ** 2 for i in range(2, int(math.sqrt(max_num)) + 1)]

# 제곱ㄴㄴ수들의 리스트. 일단 모든 수가 제곱ㄴㄴ수라고 가정함
non_squares = [1] * (max_num - min_num + 1)

# min_num 이상 max_num 이하의 범위에서 숫자 하나씩 꺼내옴
for square in squares:
    # square 이상의 최소의 min_num의 배수 x를 구하기 위함
    x = math.ceil(min_num / square) * square
    while x <= max_num:
        # non_squares 배열에서 x-min_num 만큼 접근해서 값을 0으로 바꿔줌
        non_squares[x - min_num] = 0
        x += square

# 최종적으로 non_squares 배열에서 1의 개수를 세어주면 됨
print(sum(non_squares))
