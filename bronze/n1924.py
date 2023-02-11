'''
2023.2.11
1924 - 2007년
'''
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

m, d = map(int, input().split())
day = 0

for i in range(m - 1):
    day = day + month[i]
day = (day + d) % 7
print(week[day])
