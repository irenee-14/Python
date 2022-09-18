'''
2022.9.18
2775 - 부녀회장이 될테야
'''

case = int(input())

for _ in range(case):
    k = int(input())
    n = int(input())
    room = [i for i in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            room[j] += room[j-1]
    print(room[-1])



