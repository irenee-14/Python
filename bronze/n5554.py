'''
2022.12.12
5554 - 심부름 가는 길
'''

sec = 0
for _ in range(4):
    sec += int(input())
print(int(sec/60))
print(sec%60)