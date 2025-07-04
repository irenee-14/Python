'''
2025.7.4
11966 - 2의 제곱인가?
'''

N = int(input())
squares = [2**i for i in range(31)]

if N in squares:
    print(1)
else:
    print(0)