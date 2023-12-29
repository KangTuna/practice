#1 7 19 37 61
#1 2~7 8~19 20~37 38~61
#0 6 12 18 24  


num = int(input()) # 13
check = num # 13
temp = 1
prev = 1
i = 6
count = 1
if num == 1:
    count = 1
else:
    while num > temp:
        prev = temp
        temp = i + prev
        i += 6
        count += 1

print(count)

