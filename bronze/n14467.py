'''
2023.4.7
14467 - 소가 길을 건너간 이유 1
'''

n = int(input())
cow = {}
count = 0

for i in range(n):
    index, pos = map(int, input().split())
    if index not in cow:
        cow[index] = pos
    else:
        if cow[index] != pos:
            count += 1
            cow[index] = pos
print(count)
