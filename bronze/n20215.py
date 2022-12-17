'''
2022.12.17
20215 - cutting corners
'''

w, h = map(int, input().split())
res = w + h - (w**2 + h**2)**0.5
print(res)