'''
2024.12.17
10811 - 바구니 뒤집기
'''

N, M = map(int, input().split())
basket = [i for i in range(1, N + 1)]
tmp = 0

for x in range(M):
    i, j = map(int, input().split())
    tmp = basket[i - 1:j]
    tmp.reverse()
    basket[i-1:j] = tmp

for x in range(N):
  print(basket[x], end=" ")