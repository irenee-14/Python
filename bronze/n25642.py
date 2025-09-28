'''
2025.9.28
25642 - 젓가락 게임
'''

A, B = map(int, input().split())
while 1 :
    B += A
    if B >= 5 :
        print('yt')
        break
    A += B
    if A >= 5 :
        print('yj')
        break