'''
2022.11.9
1874 - 스택수열
'''
import sys
input = sys.stdin.readline

n = int(input())
count = 0
stack = []
result = []
check = 0

for i in range(n):
    x = int(input())

    while count < x:
      count += 1
      stack.append(count)
      result.append("+")

    if stack[-1] == x:
        stack.pop()
        result.append("-")
    else:
        check = 1
        break

if check == 1:
    print("NO")
else:
    print(*result, sep="\n")
