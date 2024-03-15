'''
2024.2.18
18322 - Word Processor
'''

n, k = map(int, input().split())
line = list(map(str, input().split()))

cnt = 0

for i in range(len(line)):
    size = len(line[i])
    
    if cnt + size > k:
        print('\n' + line[i], end='')
        cnt = size
    else:
        if cnt != 0:
            print(' ', end='')
        print(line[i], end='')
        cnt += size
        

