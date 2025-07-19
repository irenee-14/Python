'''
2025.7.19
20540 - 연길이의 이상형
'''

s = input()
li = ['E', 'I', 'S', 'N', 'T', 'F', 'J', 'P']
for c in s:
    li.remove(c)
res = ''.join(li)
print(res)