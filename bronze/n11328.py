'''
2025.5.26
11328 - Strfry
'''

for i in range(int(input())):
    a, b = map(sorted, list(input().split()))
    if a == b:
        print('Possible')
    else:
        print('Impossible')