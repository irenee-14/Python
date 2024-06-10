'''
2024.6.10
1718 - 암호
'''

str = input()
key = input()

res = ''
for i in range(len(str)):
    if str[i] == ' ':
        res += ' '
        continue
    tmp = ord(str[i]) - ord(key[i % len(key)])
    if tmp < 1:
        tmp += 26
    res += chr(tmp + 96)
print(res)