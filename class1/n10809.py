'''
2022.9.12
10809 - 알파벳 찾기
'''

word = input()
alpha_list = [-1 for i in range(26)]

for i in range(len(word)):
    for j in range(26):
        if alpha_list[j] == -1 and word[i] == chr(j+97):
            alpha_list[j] = i
print(*alpha_list, sep=' ')

'''
word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x))) 
'''