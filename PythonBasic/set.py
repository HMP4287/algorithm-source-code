# X 중복 X 순서
# 리스트 혹은 문자열을 이용해서 초기화할 수 있다.
# set(), 중괄호 {}

data = set([1, 1, 2, 2, 3])
print(data)

data = {1, 2, 2, 3}
print(data)

a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

print(a|b)
print(a&b)
print(a-b)

# add, update (여러개), remove

