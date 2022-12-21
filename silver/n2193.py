'''
2022.12.21
2193 - 이친수
'''

n = int(input())

arr = [0, 1, 1]
for i in range(3, 91):
    arr.append(arr[i-2] + arr[i-1])
print(arr[n])