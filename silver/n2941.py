'''
2023.3.8
2941 - 크로아티아 알파벳
'''

word = input()

cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", 'z=']
cnt = 0

for x in cro:
    word = word.replace(x, '*')
print(len(word))