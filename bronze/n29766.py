'''
2025.7.2
29766 - DKSH 찾기
'''

word = input()
res = 0

for i in range(len(word)-3):
    if word[i:i+4] == "DKSH":
        res += 1

print(res)
