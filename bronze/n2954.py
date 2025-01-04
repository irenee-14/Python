'''
2024.1.4
2954 - 창영이의 일기장
'''

sentence = input()
i = 0
vowels = ['a', 'e', 'i', 'o', 'u']
while i < len(sentence):
    print(sentence[i], end='')
    if sentence[i] in vowels:
        i += 2
    i += 1