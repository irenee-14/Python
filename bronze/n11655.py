'''
2023.4.12
11655 - ROT13
'''

s = input()
res = []
for i in s:
    if i.isupper():
        if (65 <= ord(i) <= 77):
            res.append(chr(ord(i) + 13))  # A ~ M
        else:
            res.append(chr(ord(i) - 13))  # N ~ Z
    elif i.islower():
        if (97 <= ord(i) <= 109):
            res.append(chr(ord(i) + 13))  # a ~ m
        else:
            res.append(chr(ord(i) - 13))  # n ~ z
    else:
        res.append(i)

print(*res, sep="")