'''
2022.12.27
11726 - 타일링
'''
tile = [0, 1, 2]
for i in range(3, 1001):
  tile.append(tile[i - 2] + tile[i - 1])
n = int(input())
print(tile[n] % 10007)
