'''
2022.10.6
1966 - 프린터 큐
'''

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
    # n : 문서의 개수
    # m : 현재 queue에서 몇번 째에 놓여 있는지
    n, m = list(map(int, input().split()))
    # n개 문서의 중요도(왼쪽 0)
    que = deque(list(map(int, input().split())))
    count = 0
    # 숫자가 남은 큐 중에서 가장 큰 수가 될 때까지 검사
    while que:
        M_value = max(que)
        front = que.popleft()
        m -= 1

        # 최대값과 가장 앞 숫자가 같으면 하나 빼기
        if M_value == front:
            count += 1
            if m < 0:
                print(count)
                break
        else:
            que.append(front)
            if m < 0:
                m = len(que) - 1 #뒤로 이동
