# 내장함수
# sum, min, max, eval("(3+5)*7")
# sorted, reverse = True
# 정렬기준 -> lambda




# itertools
# 순열과 조합 순열의 수 nPr, 조합의 수 nCr
from itertools import permutations
data = ['a', 'b', 'c']
result = list(permutations(data, 3))
print(result)

from itertools import combinations
data = ['a', 'b', 'c']
result = list(combinations(data, 2))
print(result)
# 중복 순열과 중복 조합
from itertools import product
data = ['a', 'b', 'c']
result = list(product(data, repeat=2))
print(result)

from itertools import combinations_with_replacement
data = ['a', 'b', 'c']
result = list(combinations_with_replacement(data, 2))
print(result)

# Counter
from collections import Counter
counter = Counter(['red', 'blu'])
print(counter['red'])
print(counter['blu'])



# heapq
# bisect
# collections

# math
# 최대 공약수 최대 공배수
import math
# 최소 공배수 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)


a = 21
b = 14

print(math.gcd(a, b))
print(lcm(a, b))

