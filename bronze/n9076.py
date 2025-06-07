'''
2025.6.7
9076 - 점수 집계
'''

N = int(input())

for _ in range(N):
    li = list(map(int, input().split()))
    li.sort()
    if li[3] - li[1] >= 4:
        print("KIN")
    else:
        print(sum(li[1:4]))