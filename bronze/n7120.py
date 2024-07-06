'''
2024.7.6
7120 - String
'''

s = input()

import re
print(re.sub('([a-z])\\1*','\\1', s))