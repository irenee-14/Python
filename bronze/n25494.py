'''
2024.7.13
25494 - 단순한 문제 (Small)
'''
T = int(input())
while T > 0 :
    a, b, c = map(int, input().split())
    print(min(a, min(b, c)))
    T -= 1
