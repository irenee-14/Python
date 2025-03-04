'''
2025.3.4
18406 - 럭키 스트레이트
'''

N = list(map(int, input()))
A = 0
B = 0

for i in range(0, len(N) // 2):
    A += N[i]
for i in range(len(N) // 2, len(N)):
    B += N[i]

if A == B:
    print("LUCKY")
else:
    print("READY")