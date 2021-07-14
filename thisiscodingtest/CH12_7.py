import itertools

n, m = map(int, input().rstrip().split())
# 개선본
house, chi = [], []
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chi.append((r, c))

best = mid = h_shortest = 1e9  # 100이면 충분할것이라고 생각했으나 아님. 1e9를 사용하자
for i in range(m):
    result = list(itertools.combinations(chi, i + 1))
    for c in result:
        mid = 0
        # 다 더하는데, c의 요소가 여러개일 때((2, 3) or( 4, 5))는 요소들중에서 작은 값을 찾아서 더해야함
        for h in house:
            h_shortest = 1e9
            for sc in c:
                h_shortest = min(h_shortest, abs(h[0] - sc[0]) + abs(h[1] - sc[1]))
            mid += h_shortest
        best = min(best, mid)
print(best)
