'''
2025.3.12
5217 - 쌍의 합
'''

for _ in range(int(input())):
    n = int(input())
    print(f"Pairs for {n}:", end=' ')
    for i in range(1, n//2+1):
        if i != n - i:
            if i != 1:
                print(',', end=' ')
            print(i, n - i, end='')
    print()