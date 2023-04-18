'''
2023.4.18
11656 - 접미사 배열
'''
s = input()
lst = []

for i in range(len(s)):
    lst.append(s[i::])
print(*sorted(lst), sep="\n")
