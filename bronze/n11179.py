'''
2023.5.3
11179 - 2진수 뒤집기
'''
n = int(input())
# 2진수로 바꾸고 앞의 0b 잘라내기
b = str(bin(n)[2::])
rev = b[::-1]
res = int(rev, 2)
print(res)
