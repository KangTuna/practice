import sys

N = int(sys.stdin.readline().rstrip())

def recursion(s, l, r):
    global cnt
    if l >= r: 
        cnt += 1
        return 1
    elif s[l] != s[r]: 
        cnt += 1
        return 0
    else: 
        cnt += 1
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for _ in range(N):
    string = sys.stdin.readline().rstrip()
    cnt = 0
    print(isPalindrome(string),cnt)