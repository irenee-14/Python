'''
2024.7.28c
'''

y = ['A', 'B', 'C', 'D', 'E']

for i in range(3):
    s = map(int, input().split())
    print(y[3 - sum(s)])