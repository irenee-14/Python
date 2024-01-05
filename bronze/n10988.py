'''
2023.3.6
10988 - 팰린드롬인지 확인하기
'''

n = input()
new = n[::-1]
if n == new:
    print(1)
else:
    print(0)