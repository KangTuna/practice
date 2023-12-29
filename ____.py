import numpy as np
from scipy.optimize import minimize

# 주어진 데이터
x = np.array([28,32,21,25,17,23,10,26,23,13])
y = np.array([347,467,176,268,98,220,100,293,201,40])

# 최적화 함수 정의
def objective(w):
    a,b,c = w
    d = y - (a*x^2 + b*x + c)
    return np.max(np.abs(d))

# 초기 추정값
w_init = [1, 1, 1]

# 최적화 실행
result = minimize(objective, w_init, bounds=[(-np.inf, np.inf)] * 3)

# 결과 출력
a,b,c = result.x
print(f'a {a}')
print(f'b {b}')
print(f'c {c}')
