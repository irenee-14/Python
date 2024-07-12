'''
2024.4.28
9699 - RICE SACK
'''
n = int(input())
for i in range(n):
    res = map(int, input().split())
    print("Case #",i+1,": ",max(res), sep="")
