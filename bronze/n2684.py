'''
2023.4.28
2684 - 동전 게임
'''
import sys
input = sys.stdin.readline

T = int(input())
coins = ['TTT','TTH','THT','THH','HTT','HTH','HHT','HHH']
for _ in range(T):
    line = input()
    result = []
    for coin in coins:
        total = 0
        for start in range(38):
            for i in range(3):
                if line[start + i] != coin[i]:
                    total -= 1
                    break
            total += 1
        result.append(total)
    print(*result)
