'''
2024.10.14
10886 - 0 = not cute / 1 = cute
'''

N = int(input())
cute = 0

for _ in range(N):
    tmp = int(input())
    if tmp == 1:
        cute += 1

if cute > N // 2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")