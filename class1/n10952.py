'''
2022.9.13
10952 - A + B - 5
'''

while True:
    try:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        print(a + b)
    except:
        break
