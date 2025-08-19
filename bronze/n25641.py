'''
2025.8.19
25641 - 균형 잡힌 소떡소떡
'''

N = int(input())
lst = list(reversed(input()))

while 1:
    if lst.count('s') == lst.count('t'):
        break
    else:
        lst.pop(-1)
lst.reverse()
print(''.join(lst))

