'''
2025.1.3
1197 - 최소스패닝트리(다익스트라, 크루스칼)
다익스트라
'''

import heapq


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)] # 노드의 개수 + 1
visited = [0 for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append([C, B])
    graph[B].append([C, A])

answer = 0
cnt = 0

# 다익스트라로 탐색
q = [[0, 1]] # 가중치 없이 1에서 출발
while q: # q가 빌 때 까지 반복

    if cnt == N:
        break

    weight, node = heapq.heappop(q) # 우선순위 큐, 최소비용을 꺼내기
    # [node, weight] -> 노드를 기준으로 작은 것 탐색

    if visited[node] == 0:
        visited[node] = 1
        answer += weight
        cnt += 1

        for nxt in graph[node]:
            heapq.heappush(q, nxt)

print(answer)



# '''
# 2025.1.3
# 1197 - 최소스패닝트리
# 크루스칼
# '''
#
#
# def _find(x):
#     while par[x] != x: # 루트가 아니라면
#         x = par[x]
#     return x # 너가 부모면 리턴
#     # 루트 찾기
#
# def _union(a, b):
#     a = _find(a)
#     b = _find(b)
#
#     if a == b:
#         return
#     if rank[a] < rank[b]:
#         par[a] = b
#     elif rank[a] > rank[b]:
#         par[b] = a
#     else:
#         par[a] = b
#         rank[b] += 1
#
#
# N, M = map(int, input().split())
# link = [list(map(int, input().split())) for _ in range(M)]
#
# link.sort(key=lambda x:x[2]) # 가중치 기준으로 정렬
#
# par = [i for i in range(1_000_001)]
# rank = [0 for i in range(1_000_001)]
#
# ans = 0
#
# for i in range(M):
#     A = link[i][0]
#     B = link[i][1]
#     weight = link[i][2]
#
#     A = _find(A)
#     B = _find(B)
#
#     if A == B:
#         continue
#     else:
#         _union(A, B)
#         ans += weight
# print(ans)

