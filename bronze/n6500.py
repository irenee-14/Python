'''
2024.8.26
6500 - 랜덤 숫자 만들기
'''

def middle_square_method(a0):
    seen = set()  # 서로 다른 수를 저장할 집합
    current = a0  # 초기값
    while current not in seen:  # 현재 값이 이미 생성된 수가 아닐 때까지 반복
        seen.add(current)  # 현재 수를 집합에 추가
        # 현재 수를 제곱하고 길이를 2*n로 맞춘 후 가운데 n자리 추출
        squared = str(current ** 2).zfill(8)  # 2*n = 8
        current = int(squared[2:6])  # 가운데 4자리 추출
    return len(seen)  # 서로 다른 수의 개수 반환

result = []
while True:
    n = input()
    if n == '0':
        break
    tmp = int(n)
    res = middle_square_method(tmp)
    result.append(res)

for x in result:
    print(x)