'''
2022.9.9
2920 - 음계
'''

sound = list(map(int,input().split()))

if sound == sorted(sound):
    print('ascending')
elif sound == sorted(sound, reverse=True):
    print('descending')
else:
    print('mixed')
