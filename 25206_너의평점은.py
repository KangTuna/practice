import sys

input = sys.stdin.readline

def get_record(n):
    record = 0
    if n == "A+":
        record = 4.5
    elif n =="A0":
        record = 4.0
    elif n == "B+":
        record = 3.5
    elif n == "B0":
        record = 3.0
    elif n == "C+":
        record = 2.5
    elif n == "C0":
        record = 2.0
    elif n == "D+":
        record = 1.5
    elif n == "D0":
        record = 1.0
    else:
        record = 0
    return record

div = 0
total_score = 0
for _ in range(20):
    title,credit,record = input().rstrip().split()
    credit = float(credit)
    if record == "P":
        continue
    else:
        score = get_record(record)
        div += credit
        total_score += score*credit

print(round(total_score/div,6))


    