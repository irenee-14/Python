'''
2022.10.8
10816 - 숫자카드 2
'''
from collections import Counter
import sys
input = sys.stdin.readline

card = []
find = []
result = []

N = int(input())
card = list(map(int, input().split()))
M = int(input())
find = list(map(int, input().split()))

card_sort = Counter(card)
for letter in find:
    if letter not in card_sort:
        result.append(0)
    else:
        result.append(card_sort[letter])
print(*result)
