'''
2024.8.12
1668 - 트로피 진열
'''

def count(block):
    max_h = -1
    cnt = 0

    for i in block:
        if max_h < i:
            max_h = i
            cnt += 1
    return cnt

n = int(input())
block = []
for i in range(n):
    block.append(int(input()))
print(count(block))
print(count(reversed(block)))