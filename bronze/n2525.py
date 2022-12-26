'''
2022.12.26
2525 - 오븐 시계
'''

h, m = map(int, input().split())
t = int(input())

time = m + t
if time >= 60:
    h += time//60
    time %= 60
print(h%24, time)