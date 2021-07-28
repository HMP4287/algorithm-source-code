from collections import deque
a = input()
b = input()
a_arr = [deque() for _ in range(26)]  # 65 - 90인데 넉넉하게 100만큼
b_arr = [deque() for _ in range(26)]
b_order = []
for i in range(len(a)):
    a_arr[ord(a[i]) - 65].append(i)
for i in range(len(b)):
    b_arr[ord(b[i]) - 65].append(i)
    b_order.append(ord(b[i]) - 65)

idx = 0
total = 0
for i in b_order:
    # print(i)
    # print()
    # print(i)
    # print(])
    if a_arr[i][0] < b_arr[i][0]:
        total += 1
        # print("a = ", a_arr[i][0], "b = ", b_arr[i][0])
        # print(total)
        b_arr[i].popleft()
        # a_arr[i].popleft()
    else:
        # print("a = ", a_arr[i][0], "b = ", b_arr[i][0])
        # print(total)
        b_arr[i].popleft()

    idx += 1
# print()
print(total)
