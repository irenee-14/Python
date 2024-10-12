'''
2024.10.12
14215 - 세 막대
'''

line = list(map(int, input().split()))
line.sort()
if line[0] + line[1] > line[2]:
    print(sum(line))
else:
    print((line[0]+line[1]) * 2 - 1)
