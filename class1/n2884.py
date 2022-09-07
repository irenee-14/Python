'''
2022.9.7
2884 - 알람시계
'''

n, m = map(int, input().split())
time = 24 * 60 + (60 * n + m) - 45
new_m = time % 60
new_n = (time / 60) % 24
print(int(new_n), new_m)
