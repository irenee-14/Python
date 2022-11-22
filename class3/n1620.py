'''
2022.11.22
1620 - 나는야 포켓몬 마스터 이다솜
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic_digit = {}
dic_name = {}
tmp = 0
for i in range(1, N+1):
    tmp = input().strip()
    dic_digit[i] = tmp
    dic_name[tmp] = i
    
for _ in range(M):
    t = input().strip()
    if t.isdigit():
        print(dic_digit[int(t)])
    else:
        print(dic_name[t])
        
