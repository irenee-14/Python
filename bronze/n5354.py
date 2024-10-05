'''
2024.10.5
5354 - J박스
'''

n = int(input())
for _ in range(n):
    n = int(input())
    if n < 3:
        for i in range(n):
            print('#' * n)
        print()
    else:
        print('#' * n)
        for i in range(n-2):
            print('#' + 'J' * (n-2) + '#')
        print('#' * n, '\n')