'''
2023.4.10
10769 - 행복한지 슬픈지
'''

line = input()

happy = line.count(":-)")
sad = line.count(":-(")

if happy == 0 and sad == 0:
    print("none")
elif happy > sad:
    print("happy")
elif happy == sad:
    print("unsure")
elif happy < sad:
    print("sad")

