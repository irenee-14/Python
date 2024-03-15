'''
2024.2.5 
1238 - 파티 (다익스트라 - dijkstra)
'''
import heapq 

def dijkstra(start):
    visited = [0] * (N + 1)
    dist = [float('inf')] * (N + 1)
    # 시작으로 가기 위한 최단경로 0으로 설정해서 큐에 삽입
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    
    while q: 
        # 가장 최단 거리 노드에 대한 정보
        distance, now = heapq.heappop(q)
        if dist[now] >= distance:
            # i[0] : 인접 노드, i[1] : 비용
            for i in road[now]:
                cost = distance + i[1]
                if cost < dist[i[0]]:
                    dist[i[0]] = cost 
                    heapq.heappush(q, (cost, i[0]))
    return dist


N, M, X = map(int, input().split())
road = [[] for _ in range(N + 1)]
for i in range(M):
    x, y, t = map(int, input().split())
    road[x].append([y, t])

# X에서 모든 노드로    
res = dijkstra(X)
res[0] = 0

# 각 노드에서 X로 
for i in range(1, N + 1):
    if i != X:
        tmp = dijkstra(i)
        res[i] += tmp[X]
        
print(max(res))

# https://week-book.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-2%EA%B0%80%EC%A7%80-%EB%B0%A9%EB%B2%95%EC%9C%BC%EB%A1%9C-%EA%B5%AC%ED%98%84-for-heapq

# ------------------------------------------------
# ------------ heap 사용 X, 시간 초과 ---------------
# def party(x):
#     visited = [0] * (N + 1)
#     dist = [float('inf')] * (N + 1)
#     dist[x] = 0
    
#     for _ in range(N):
#         # 최소 비용 노드 탐색
#         minPos = -1
#         minD = float('inf')
#         for k in range(1, N + 1):
#             if not visited[k] and dist[k] < minD:
#                 minD = dist[k]
#                 minPos = k 
#         visited[minPos] = 1 
        
#         for end, val in road[minPos]:
#             if not visited[end] and val + dist[minPos] < dist[end]:
#                 dist[end] = val + dist[minPos]
#     return dist
    

# N, M, X = map(int, input().split())
# road = [[] for _ in range(N + 1)]
# for i in range(M):
#     x, y, t = map(int, input().split())
#     road[x].append([y, t])

# # X에서 모든 노드로    
# res = party(X)
# res[0] = 0

# # 각 노드에서 X로 
# for i in range(1, N + 1):
#     if i != X:
#         tmp = party(i)
#         res[i] += tmp[X]
        
# print(max(res))
