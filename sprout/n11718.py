'''
2023.1.4
11718 - 그대로 출력하기
'''
while True:
    try:
        print(input())
    except EOFError:
        break
