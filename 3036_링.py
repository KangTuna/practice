import sys
from fractions import Fraction

input = sys.stdin.readline

N = int(input().rstrip())
data = list(map(int,input().rstrip().split()))
ring_size = data.pop(0)
ans = []
for i in data:
    a = Fraction(ring_size,i)
    print(f"{a.numerator}/{a.denominator}")

