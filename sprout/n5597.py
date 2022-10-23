'''
2022.10.23
5597 - 과제 안 내신 분..?
'''

homework = [i for i in range(1,31)]
for i in range(28):
    apply = int(input())
    homework.remove(apply)
print(min(homework))
print(max(homework))
