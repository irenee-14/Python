'''
2022.9.20
1181 - 단어 정렬
'''

import sys

n = int(input())
word_list = []

for i in range(n):
#    word_list.append(input())
    word_list.append(sys.stdin.readline().strip())
word_list = list(set(word_list))
word_list.sort()
word_list.sort(key=len)
for i in word_list:
    print(i)
