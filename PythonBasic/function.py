def add(a, b):
    return a + b


# 파라미터 지정 가능
# result = add(b=3, a=7)

# global 키워드
a = 0
# list = [1, 2, 4, 4, 5]


def func():
    global a  # 전역변수를 참조해 사용하려면 global 키워드 사용해야 함
    a += 1


def func2():
    print(a + 20)  # 이건 global 키워드 안써도 됨


def func3():
    list.append(1)  # 전역변수 리스트 메소드 호출 문제없음 but 지역변수 > 전역변수
    list.append(5)


def multiReturn():
    a = 1
    b = 2
    c = 3
    return a, b, c  # 패킹


a, b, c = multiReturn()  # 언 패킹
print(a, b, c)

# 람다 표현식 함수 자체를 입력으로 받는 또 다른 함수나 한번 사용하고 말 함수
print((lambda a, b: a + b)(3, 7))

# example
arr = [('hong', 50), ('sam', 20)]


def my_key(x):
    return x[1]


print(sorted(arr, key=my_key))
print(sorted(arr, key=lambda x: x[1]))

list1 = [1,2,3,4]
list2 = [1,2,3,4]
list3 = [1,2,3,7]
result = map(lambda a,b,c: a + b + c, list1, list2, list3)
print(list(result))
