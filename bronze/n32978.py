'''
2025.10.20
32978 - 아 맞다 마늘
'''

N = int(input())
Pasta = input().split()
HyunBin = input().split()

for p in Pasta:
    if p not in HyunBin:
        print(p)
        break