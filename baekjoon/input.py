# input() 함수는 '한 줄'의 '문자열'을 입력 받음
# map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 떄 사용
data = list(map(int, input().split()))
data2 = (map(int, input().split()))

print(data)
print(data2)

a, b, c = map(int, input().split())
