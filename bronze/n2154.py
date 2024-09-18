'''
2024.9.18
2154 - 수 이어 쓰기 3
'''

N = int(input())
s = ''
for i in range(1, N + 1):
    s += str(i)

print(s.index(str(N)) + 1)