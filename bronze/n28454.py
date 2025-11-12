'''
2025.11.12
28454 - Gift Expire Date
'''

import datetime
# now = str(input())
now = datetime.datetime.strptime(str(input()), "%Y-%m-%d")
N = int(input())
cnt = 0
for i in range(N):
    new = datetime.datetime.strptime(str(input()), "%Y-%m-%d")
    if new >= now:
        cnt += 1
print(cnt)