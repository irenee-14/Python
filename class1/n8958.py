'''
2022.9.10
8958 - OX퀴즈
'''

num = int(input())
arr = []

for i in range(num):
    arr = input()
    tmp = 0
    result = 0
    for j in range(len(arr)):
        if arr[j] == 'O':
            tmp += 1
        else:
            tmp = 0
        result += tmp
    print(result)
