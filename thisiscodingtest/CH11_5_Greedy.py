# import sys
#
# n, m = sys.stdin.readline().rstrip().split()
# data = list(map(int, sys.stdin.readline().rstrip().split()))
#
# cnt = 0
# for i in range(len(data)):
#     for j in range(i + 1, len(data)):
#         if data[i] == data[j]:
#             continue
#         cnt += 1
#
# print(cnt)

# 개선한 코드
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))
nums = [0]*(m+1)

for i in data:
    nums[i] += 1

for i in nums:
    print(i)

total = 0
for i in range(1, m+1):
    n -= nums[i]  # 자기자신
    total += nums[i] * n

print(total)
