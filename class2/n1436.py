'''
2022.9.16
1436 - 영화감독 숌
'''

n = int(input())
count = 0
num = 1

while True:
    if "666" in str(num):
        count += 1
    if count == n:
        print(num)
        break
    num += 1