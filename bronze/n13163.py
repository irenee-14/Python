'''
2025.5.21
13163 - 닉네임에 갓 붙이기
'''

N = int(input())

for _ in range(N):
    nickName = input().split()
    result = "god"

    for i in range(1, len(nickName)):
        result += nickName[i]

    print(result)