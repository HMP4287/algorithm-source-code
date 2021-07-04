# 리스트
# 리스트를 0으로 10개 초기화
a = [0] * 10
print(a)

# 음수 인덱싱이 가능
print(a[-3])

# 슬라이싱
print(a[1:4])

# 리스트 컴프리헨션
array = [i for i in range(10)] # 이것은 배열 ? ? ?
print(array)
array = [i for i in range(20) if i % 2 == 1]

# 2차원 리스트 초기화 시  N X M
n = m = 10
array = [[0]*m for _ in range(n)]
print(array)

# 언더바 반복을 수행하되 반복을 위한 변수의 값을 무시하고 할 때 사용
for _ in range(5):
    print("Hi")

# append, sort, sort(reverse = True), reverse, insert, count (특정 값이 a.count(3) 3인 데이터 개수 세기), remove

a = [i for i in range (1, 10)]
remove_set = {2, 4, 6, 8}

result = [i for i in a if i not in remove_set]
print(result)









