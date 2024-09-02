'''
2024.9.2
10768 - 특별한 날
'''

m = int(input())
d = int(input())
if m < 2:
    print("Before")
elif m == 2:
    if d == 18:
        print("Special")
    elif d > 18:
        print("After")
    else:
        print("Before")
else:
    print("After")