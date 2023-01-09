'''
2023.1.9
5430 - AC
'''

from collections import deque

T = int(input())
for i in range(T):
    fun = input()
    n = int(input())
    nums = deque(input()[1:-1].split(','))
    if n == 0:
        nums = []

    check = 0
    for j in fun:
        if j == 'R':
            check += 1
        elif j == 'D':
            if nums:
                if check % 2 == 0:
                    nums.popleft()
                else:
                    nums.pop()
            else:
                print("error")
                break
    else:
        if check % 2 != 0:
            nums.reverse()
        print("[" + ",".join(nums) + "]")

