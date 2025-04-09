'''
2025.4.9
11637 - 인기 투표
'''

for _ in range(int(input())):
    n = int(input())
    vote = []

    for i in range(n):
        vote.append(int(input()))
    tmp = sorted(vote, reverse=True)
    if len(tmp) > 1 and tmp[0] == tmp[1]:
        print('no winner')
    elif sum(vote) - tmp[0] < tmp[0]:
        print('majority winner', vote.index(tmp[0]) + 1)
    else:
        print('minority winner', vote.index(tmp[0]) + 1)

