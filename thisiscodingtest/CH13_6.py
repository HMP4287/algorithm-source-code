import itertools
from collections import deque
import copy

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

X = 0
T = 1
S = 2
O = 3

n = int(input())
pos = []

map_arr = [[0] * n for _ in range(n)]
tea_list = []
stu_list = []
base_visited = [[False] * n for _ in range(n)]
visited = []

for i in range(n):
    d = input().split()
    for j in range(len(d)):
        if d[j] == "X":
            map_arr[i][j] = 0
        elif d[j] == "T":
            map_arr[i][j] = 1
            base_visited[i][j] = True
            tea_list.append((i, j))
        else:
            map_arr[i][j] = 2
            stu_list.append((i, j))
        pos.append((i, j))


def bfs_v2(x, y):
    if x >= n or y >= n or x < 0 or y < 0:
        return
    # if not visited[x][y]:
    #     visited[x][y] = True
    for i in range(4):
        if x + dx[i] >= n or y + dy[i] >= n or x + dx[i] < 0 or y + dy[i] < 0:
            if not visited[x + dx[i]][y + dy[i]]:
                bfs_v2(x + dx[i], y + dy[i])
                visited[x + dx[i]][y + dy[i]] = True


def bfs_v3(x, y):
    s = []
    s.append((x, y))
    while s:
        p = s.pop()
        for i in range(4):
            next_x = p[0] + dx[i]
            next_y = p[1] + dy[i]
            if next_x >= n or next_y >= n or next_x < 0 or next_y < 0:
                if not visited[next_x][next_y]:
                    s.append(next_x, next_y)
                    visited[next_x][next_y] = True


def bfs_v4(x, y, path):
    # if x >= n or y >= n or x < 0 or y < 0:
    #     return
    next_x = x + dx[path]
    next_y = y + dy[path]
    if next_x < n and next_y < n and next_x >= 0 and next_y >= 0:
        if not visited[next_x][next_y]:
            visited[next_x][next_y] = True
            bfs_v4(next_x, next_y, path)
    return

    # while s:
    #     p = s.pop()
    #     for i in range(4):
    #         next_x = p[0] + dx[i]
    #         next_y = p[1] + dy[i]
    #         if next_x >= n or next_y >= n or next_x < 0 or next_y < 0:
    #             if not visited[next_x][next_y]:
    #                 s.append(next_x, next_y)
    #                 visited[next_x][next_y] = True


def bfs(visited, x, y, t):
    q = deque([(x, y)])

    while q:
        p = q.popleft()
        for idx in range(4):
            next_x = p[0] + dx[idx]
            next_y = p[1] + dy[idx]
            if next_x >= n or next_y >= n or next_x < 0 or next_y < 0:
                continue
            if visited[next_x][next_y]:
                continue
            else:
                visited[next_x][next_y] = True
                q.append((next_x, next_y))
                if t == 1:
                    print("n = ", end=" ")
                    print(next_x, next_y)
    if t == 1:
        print("done")


# 3개 장애물 설치 모든 경우의 수, 6*6중에서 3개 36c3, X 중복
result = list(itertools.combinations(pos, 3))
ok = False
for wall_1, wall_2, wall_3 in result:

    if map_arr[wall_1[0]][wall_1[1]] != X or map_arr[wall_2[0]][wall_2[1]] != X or map_arr[wall_3[0]][wall_3[1]] != X:
        continue
    visited = copy.deepcopy(base_visited)
    # 벽 세우기 1,1 3,0 2,2
    visited[wall_1[0]][wall_1[1]] = True
    visited[wall_2[0]][wall_2[1]] = True
    visited[wall_3[0]][wall_3[1]] = True

    for tea_pos in tea_list:
        for i in range(4):
            bfs_v4(tea_pos[0], tea_pos[1], i)
    tf = True
    for stu_pos in stu_list:
        if visited[stu_pos[0]][stu_pos[1]]:
            tf = False
            break
    if tf:
        ok = True
        break

if ok:
    print("YES")
else:
    print("NO")
