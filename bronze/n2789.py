'''
2024.7.4
2789 - 유학 금지
'''

data = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

value = input()
for i in range(len(value)) :
  if value[i] not in data :
    print(value[i], end='')