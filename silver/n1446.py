'''
2024.4.9
1446 - 지름길
'''

N, D = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

distance = [i for i in range(D + 1)]

for i in range(D + 1):
    distance[i] = min(distance[i], distance[i - 1] + 1)
    for start, end, dist in graph:
        if i == start and end <= D and distance[i] + dist < distance[end]:
            distance[end] = distance[start] + dist
print(distance[D])