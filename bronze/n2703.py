'''
2025.2.2
2703 - Cryptoquote
'''

t = int(input())

for i in range(t):
    q = input()
    a = input()

    for x in q:
        if x == ' ':
            print(' ', end='')
            continue
        else:
            print(a[ord(x) - ord('A')], end='')
    print()