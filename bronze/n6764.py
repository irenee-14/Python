'''
2024.6.13
6764 - Sounds fishy!
'''

arr = [int(input()) for _ in range(4)]
x = 0
for i in range(3):
    if arr[i + 1] > arr[i]:
        x = x + 1
    elif arr[i + 1] < arr[i]:
        x = x - 1

if len(set(arr)) == 1:
    print("Fish At Constant Depth")
elif x == 3:
    print("Fish Rising")
elif x == -3:
    print("Fish Diving")
else:
    print("No Fish")