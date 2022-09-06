'''
2577 - 숫자의 개수
2022.9.6
'''

'''
n_sum = 1
sum_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(3):
    n_sum *= int(input())
while int(n_sum) > 0:
    i = 0
    for i in range(10):
        if int(n_sum % 10) == i:
            sum_list[i] += 1
    n_sum /= 10
print(*sum_list, sep='\n')
'''

a = int(input())
b = int(input())
c = int(input())

res = list(str(a * b * c))
for i in range(10):
    print(res.count(str(i)))