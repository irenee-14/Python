'''
2023.2.12
5622 - 다이얼
'''

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()

sec = 0
for d in dial:
    for i in d:
        for x in word:
            if i == x:
                sec += dial.index(d) + 3
print(sec)