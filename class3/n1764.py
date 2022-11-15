'''
2022.11.15
1764 - 듣보잡
'''

N, M = map(int, input().split())
hear = set()
see = set()

for _ in range(N):
    hear.add(input())
for _ in range(M):
    see.add(input())

result = sorted(list(hear & see))

print(len(result))
for i in result:
    print(i)
