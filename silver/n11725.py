'''
2024.12.30
11725 - 트리 부모 찾기
'''
import sys
sys.setrecursionlimit(99999)

N = int(input())

graph = [[] for _ in range(N + 1)]
parent = [0 for _ in range(N + 1)]
child = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


def recur(node, prv):

    for nxt in graph[node]:
        if nxt == prv:
            continue
        parent[nxt] = node
        recur(nxt, node)
    # child[prv] += 1

recur(1, 0)
# print(par)
# print(child_num)
print(*parent[2::], sep="\n")

