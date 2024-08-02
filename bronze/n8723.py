'''
2024.8.2
8723 - Patyki
'''

stick = sorted(map(int, input().split()))

if stick[0] == stick[1] == stick[2]:
    print(2)
elif stick[0] ** 2 + stick[1] ** 2 == stick[2]** 2:
    print(1)
else:
    print(0)