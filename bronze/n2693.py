'''
2024.9.23
2693 - N번째 큰 수
'''

T = int(input())

for i in range(T):
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(A[2])
