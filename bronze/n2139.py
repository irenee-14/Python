'''
2024.7.7
2139 - 나는 너가 살아온 날을 알고 있다
'''

import datetime

while True:
    day, month, year = map(int, input().split())
    if day == 0 and month == 0 and year == 0:
        exit(0)
    input_day = datetime.datetime(year=year, month=month, day=day)
    std_day = datetime.datetime(year=year, month=1, day=1)

    datetime_info = input_day - std_day

    print(datetime_info.days + 1)
