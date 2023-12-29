import sys

input = sys.stdin.readline

def contoa(dash):
    if dash == 1:
        return '-'
    thislen = dash//3
    return contoa(thislen) + ' '*thislen + contoa(thislen)

while True:
    try:
        n = int(input().rstrip())
        length = 3 ** n
        print(contoa(length))
    except:
        break
    

