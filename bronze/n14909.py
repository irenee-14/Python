'''
2025.10.3
14909 - 양수 개수 세기
'''

li = list(map(int, input().split()))
cnt = len([n for n in li if n > 0])
print(cnt)