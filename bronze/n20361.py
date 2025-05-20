'''
2025.5.20
20361 - 일우는 야바위꾼
'''
import sys

input = sys.stdin.readline

N, X, K = map(int, input().split())

cups = [0] * (N + 1)
cups[X] = 1

for _ in range(K):
    A, B = map(int, input().split())

    cups[A], cups[B] = cups[B], cups[A]

print(cups.index(1))