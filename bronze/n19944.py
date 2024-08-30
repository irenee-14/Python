'''
2024.8.30
19944 - 뉴비의 기준은 뭘까?
'''

N, M = map(int, input().split())
if M <= 2:
    print("NEWBIE!")
elif M <= N:
    print("OLDBIE!")
else:
    print("TLE!")