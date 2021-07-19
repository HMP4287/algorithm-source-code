# input() 함수는 '한 줄'의 '문자열'을 입력 받음
# map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 떄 사용

# data = list(map(int, input().split()))
# data2 = (map(int, input().split()))
#
# print(data)
# print(data2)
#
# a, b, c = map(int, input().split())

# 빠른 입력 sys.stdin.readline() + rstrip()은 줄바꿈 제거
# print("hi")
# import sys
# data = list(map(int, sys.stdin.readline().rstrip().split()))
# print(data)


# Output
print(7, end=" ")
print(7, end=" ")
answer = 7
print("정답은 " + str(answer) + " 입니다", end="\n")

# f-string
answer = 7
print(f"정답은 {answer} 입니다")

n, k = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
