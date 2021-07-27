T = int(input())
for _ in range(T):
    N = int(input())
    COINS = list(map(int, input().split()))
    M = int(input())
    coin_count = [0] * (M + 1)
    coin_count[0] = 1
    for coin in COINS:
        for i in range(1, M + 1):
            if i - coin >= 0:
                coin_count[i] += coin_count[i - coin]
    print(coin_count[M])
    # V 1.0
    # for i in range(N):
    #     result = list(itertools.combinations(COINS, i+1))
    #     for combination in result:
    #         print(combination)
    #         # break
    #         total = 0
    #         for num in combination:
    #             total += num
    #         # 1
    #         # print(total)
    #         j = total
    #         while j < M + 1:
    #             coin_count[j] += 1
    #             j += total
    #         # print(coin_count)
    #         # break
    #     # break
    #
    # print(coin_count[M])
