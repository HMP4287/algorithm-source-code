import heapq
N = int(input())
cards = []
for _ in range(N):
    cards.append(int(input()))

# 제귀 ?
if N == 1:  # ex) N==1 cards = [1]일때 비교 횟수는 0임.
    print(0)
elif N == 2:
    print(cards[0] + cards[1])
else:
    result = 0
    heapq.heapify(cards)
    for _ in range(N-1):  # 연산 횟수는 총 N-1
        a, b = heapq.heappop(cards), heapq.heappop(cards)
        tot = a + b
        result += tot
        heapq.heappush(cards, tot)
    print(result)





    # V1.0
    # cards.sort()
    # total = 0
    # prev = 0
    # for i in range(N-1):
    #     added = cards[i] + cards[i + 1]
    #     total += added
    #     cards[i+1] = added
    #     prev = added
    # print(total)





