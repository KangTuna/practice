import sys

input = sys.stdin.readline

current_time = input().rstrip().split(':')
throw_time = input().rstrip().split(':')

current_hour = int(current_time[0])
current_minute = int(current_time[1])
current_second = int(current_time[2])

throw_hour = int(throw_time[0])
throw_minute = int(throw_time[1])
throw_second = int(throw_time[2])

current_total_seconds = current_hour * 3600 + current_minute * 60 + current_second
throw_total_seconds = throw_hour * 3600 + throw_minute * 60 + throw_second

if current_total_seconds == throw_total_seconds:
    print("24:00:00")
elif current_total_seconds < throw_total_seconds:
    remaining_seconds = throw_total_seconds - current_total_seconds
    remaining_hour = remaining_seconds // 3600
    remaining_minute = (remaining_seconds % 3600) // 60
    remaining_second = (remaining_seconds % 3600) % 60
    print(f"{remaining_hour:02d}:{remaining_minute:02d}:{remaining_second:02d}")
else:
    remaining_seconds = (24 * 3600 - current_total_seconds) + throw_total_seconds
    remaining_hour = remaining_seconds // 3600
    remaining_minute = (remaining_seconds % 3600) // 60
    remaining_second = (remaining_seconds % 3600) % 60
    print(f"{remaining_hour:02d}:{remaining_minute:02d}:{remaining_second:02d}")