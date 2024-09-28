'''
2024.9.28
5988 - 홀수일까 짝수일까
'''

n = int(input())
for i in range(n):
    k = int(input())
    if k % 2 == 0:
        print('even')
    else:
        print('odd')