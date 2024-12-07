'''
2024.12.7
2052 - 지수 연산
'''

n = int(input())
tmp = "%.300f" % 2 ** -n

end = len(tmp)
for i in range(end - 1, 1, -1):
    if tmp[i] != '0':
        end = i
        break
print(tmp[:end + 1])