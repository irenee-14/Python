'''
2023.3.27
16204 - 카드 뽑기
'''
N, M, K = map(int, input().split())
print(min(M, K) + N - max(M, K)) 
