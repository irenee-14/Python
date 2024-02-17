'''
2024.2.17
1043 - 거짓말 (set)
'''
from collections import deque

N, M = map(int, input().split())
know = list(map(int, input().split()))[1:]
party = []

# know에 존재하지 않고, know에 있는 사람과 만나지 않아야 함
# 각 
meet = list({0} for _ in  range(N + 1))
for i in range(M):
    party.append(list(map(int, input().split()))[1:])
    # x가 만나는 사람들 모두 저장
    for x in party[i]:
        for y in party[i]:
            meet[x].add(y)

que = deque(know)
# 진실을 아는 사람들을 돌면서, 그사람들이 만나는 사람들 knnow에 추가 
while que:
    tmp = que.popleft()
    
    for someone in meet[tmp]:
        # tmp가 만난 사람들 중에 know가 있으면 continue
        if someone in know:
            continue
        else:
            know.append(someone)
            que.append(someone)

res = 0
for i in range(M):
    # & : 교집합,
    if list(set(know) & set(party[i])):
        continue
    else:
        res += 1 
print(res)
