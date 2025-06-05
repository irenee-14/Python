'''
2025.6.5
5598 - 카이사르 암호
'''

li = list(input())
for i in range(len(li)):
    k = ord(li[i]) - 3
    if k < ord('A'):
        k += 26
    li[i] = chr(k)
print(''.join(li))