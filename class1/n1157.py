'''
1157 - 단어 공부
2022.9.3
'''

word = input().upper()
word_list = list(set(word))
dic = []

for i in word_list:
    dic.append(word.count(i))
if dic.count(max(dic)) > 1:
    print("?")
else:
    print(word_list[dic.index(max(dic))])

