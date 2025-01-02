'''
2025.1.2
1717 - 집합의 표현
'''

import sys
sys.setrecursionlimit(99999)
def _union(A, B):  # 최대 높이를 확인해서 합쳐준다! 효과적으로
    A = _find(A)
    B = _find(B)

    if A < B:
        par[B] = A
    else:
        par[A] = B


def _find(A):
    if par[A] == A:  # 스스로를 부모로 칭하고 있다면 == 부모가 없다면 == 자기가 루트
        return A
    else:
        par[A] = _find(par[A])
        return par[A] # 내 부모의 부모를 찾아서 리턴



N, M = map(int, input().split())

par = [i for i in range(N + 1)]
# [0, 1, 2, 3, 4, 5, 6, 7] 스스로를 부모로 칭하도록 만들어 둠
rank = [0 for i in range(N + 1)]

for i in range(M):
    X, A, B = map(int, input().split())

    if X == 0:
        _union(A, B)

    else:
        if _find(A) == _find(B):
            print("YES")
        else:
            print("NO")
