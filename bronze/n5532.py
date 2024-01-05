'''
2023.2.21
5532 - 방학 숙제
'''

import math

sub = []
for i in range(5):
    sub.append(int(input()))
print(sub[0] - max(math.ceil(sub[1]/sub[3]), math.ceil(sub[2]/sub[4])))