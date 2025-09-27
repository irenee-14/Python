'''
2025.9.27
4592 - 중복을 없애자
'''

while True:
    try:
        tmp = list(map(int,input().split()))
        res = []
        res.append(tmp[1])
        for i in range(2, len(tmp)):
            if res[-1] != tmp[i] :res.append(tmp[i])
        for i in range(len(res)):
            print(res[i], end=' ')
        print("$")

    except:
        exit()


