'''
2025.8.14
23809 - 골뱅이 찍기 - 돌아간 ㅈ
'''

N = int(input())

for i in range(N):
    print("@" * N + " " * 3 * N + "@" * N)

for i in range(N):
    print("@" * N + " " * 2 * N + "@" * N)

for i in range(N):
    print("@" * 3 * N)

for i in range(N):
    print("@" * N + " " * 2 * N + "@" * N)

for i in range(N):
    print("@" * N + " " * 3 * N + "@" * N)