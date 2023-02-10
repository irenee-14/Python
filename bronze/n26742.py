'''
2023.1.11
26742 - Skarpetki
'''

colors = input()
n_b = 0
n_c = 0

for i in colors:
    if i == 'B':
        n_b += 1 
    elif i == 'C':
        n_c += 1
print(n_b//2 + n_c//2)
