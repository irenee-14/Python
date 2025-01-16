'''
2025.1.16
25192 - 인사성 밝은 곰곰이
'''
import sys

input = sys.stdin.readline

n = int(input())
cnt = 0
dic = set()

for i in range(n):
    s = input().rstrip()

    if s == 'ENTER':
        cnt += len(dic)
        dic = set()
    else:
        dic.add(s)
cnt += len(dic)
print(cnt)
