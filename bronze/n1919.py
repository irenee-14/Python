'''
2024.7.30
1919 - 애너그램 만들기
'''

a = input()
b = input()

alphabet = [0] * 26

for i in range(len(a)):
    alphabet[ord(a[i]) - 97] += 1
for i in range(len(b)):
    alphabet[ord(b[i]) - 97] -= 1
res = 0
for i in alphabet:
    res += abs(i)
print(res)