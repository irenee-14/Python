'''
2024.11.2
1440 - 타임머신
'''

n1, n2, n3 = map(int,input().split(":"))
cnt = 0

if n1 == 0 and n2 == 0 and n3 == 0:
    cnt += 0
if 0 < n1 < 13 and 0 <= n2 < 60 and 0 <= n3 < 60:
    cnt += 2
if 0 < n2 < 13 and 0 <= n1 < 60 and 0 <= n3 < 60:
    cnt += 2
if 0 < n3 < 13 and 0 <= n1 < 60 and 0 <= n2 < 60:
    cnt += 2

print(cnt)