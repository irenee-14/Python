'''
2023.1.23
7662 - 이중 우선순위 큐
'''

import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    max_heap = []
    min_heap = []
    visited = [0] * 1000001

    k = int(input())

    for i in range(k):
        op, n = input().split()
        if op == 'I':
            heapq.heappush(min_heap, (int(n), i))
            heapq.heappush(max_heap, (int(n) * -1, i))
            visited[i] = 1

        elif op == 'D':
            if n == '-1':
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)
            elif n == '1':
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
