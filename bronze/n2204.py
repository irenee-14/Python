'''
2023.1.18
2204 - 도비의 난독증 테스트
'''

while True:
    tmp = int(input())
    if tmp == 0:
        break
    else:
        dic = []
        for _ in range(tmp):
            dic.append(input())
        dic.sort(key = str.lower)
        print(dic[0])