'''
2024.12.26
1753 - 최단경로(다익스트라)
'''

import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
start = int(input())
links = [[] for _ in range(N + 1)]


for _ in range(M):
    A, B, C = map(int, input().split())
    links[A].append([B, C]) # 다음, 가중치

dist = [float('inf')] * (N + 1) # 엄청 큰 수 넣어두기
dist[start] = 0
# 우선순위 큐 초기화
q = []
heapq.heappush(q, [0, start])


while q:
    # 우선순위 큐를 이용해서, 거리를 보고 정렬
    # heapq.heapify(q)
    _w, node = heapq.heappop(q)

    if dist[node] < _w:
        continue
    for nxt, weight in links[node]:
        # 1. 각각의 노드에 값을 업데이트
        # 2. 만약에 여러 경로가 있다면 min 비교
        # 3. 시작점으로부터 거리 중 짧은 순서대로 탐색
        new_dist = dist[node] + weight
        if new_dist < dist[nxt]:
            dist[nxt] = new_dist
            heapq.heappush(q, [new_dist, nxt])

for i in range(1, N + 1):
    if dist[i] == float('inf'):
        print('INF')
    else:
        print(dist[i])
