'''
2023.3.15
1357 - 뒤집힌 덧셈
'''

x, y = map(str, input().split())

res = str(int(x[::-1]) + int(y[::-1]))
print(int(res[::-1]))
