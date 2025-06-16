'''
2025.6.16
17502 - 클레어와 팰린드롬
'''

N = int(input())
s = input()

palindrome = ''

for c1, c2 in zip(s, s[::-1]):
    if c1 == '?' and c2 == '?':
        palindrome += 'a'
    elif c1 == '?':
        palindrome += c2
    elif c2 == '?':
        palindrome += c1
    else:
        palindrome += c1

print(palindrome)

