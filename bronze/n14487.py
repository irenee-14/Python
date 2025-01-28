'''
2025.1.28
14487 - 욱제는 효도쟁이야!!
'''

import sys
input = sys.stdin.readline

n = int(input())
town = list(map(int, input().split()))

print(sum(town) - max(town))