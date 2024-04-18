'''
2024.4.18
1755 - 숫자놀이
'''
nums = {'1' : 'one', '2' : 'two', '3' : 'three', '4' : 'four', '5' : 'five', 
        '6' : 'six', '7' : 'seven', '8' : 'eight', '9' : 'nine', '0' : 'zero'}
        
M, N = map(int, input().split())
arr = []
for i in range(M, N + 1):
    tmp = ' '.join(nums[j] for j in str(i))
    arr.append((tmp, i))
    
arr.sort()
for i in range(len(arr)):
    print(arr[i][1], end=" ")
    if (i + 1) % 10 == 0:
        print()
