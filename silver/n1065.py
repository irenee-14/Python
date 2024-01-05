'''
2023.3.9
1065 - 한수
'''

n = int(input())

han = 0
for i in range(1, n + 1):
    num_list = list(map(int, str(i)))
    if i < 100:
        han += 1
    elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
        han += 1
print(han)
