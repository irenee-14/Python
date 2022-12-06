'''
2022.12.6
2442 - 별찍기 5
'''

n = int(input())
for i in range(n):
    res = ' '*(n-i-1)+'*'*(2*i+1)
    print(res)
