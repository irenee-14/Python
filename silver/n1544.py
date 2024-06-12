'''
2024.6.11
1544 - 사이클 단어
'''

from collections import deque

n = int(input())
word = [input() for _ in range(n)]

for i in range(n):
   que = deque(word[i])

   while True:
       que.append(que.popleft())
       tmp = "".join(que)

       if tmp == word[i]:
           break
       if tmp in word:
           index = word.index(tmp)
           word.pop(index)
           word.insert(index, word[i])

print(len(set(word)))
