# 미완성
from collections import deque

n, l, r = map(int, input().split())
map_arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_list = set()


def bfs(visited, i, j):
    q = deque([(i, j)])
    # visited[i][j] = True
    # 정확하게 move_list 에 append
    while q:
        prev = q.popleft()
        for path in range(4):
            nx = prev[0] + dx[path]
            ny = prev[1] + dy[path]
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue
            m = abs(map_arr[nx][ny] - map_arr[prev[0]][prev[1]])
            if m > r or m < l:  # 차가 l r 사이 아니라면
                continue
            if not visited[nx][ny]:
                visited[prev[0]][prev[1]] = True
                visited[nx][ny] = True
                q.append((nx, ny))
                move_list.add((prev[0], prev[1]))
                move_list.add((nx, ny))


# 하루 다 끝나고 이동시키기.
def move():
    print(move_list)
    length = len(move_list)  # len 시 팝 후 길이 다시 체크 하는지 확인  필요
    total = 0
    for i, j in move_list:
        total += map_arr[i][j]
    total //= length
    for _ in range(length):
        i, j = move_list.pop()
        map_arr[i][j] = total
    # return True  # 인구 이동 실행 완료.


count = 0
temp = 0
while True:
    visited = [[False] * n for _ in range(n)]
    # 1일
    for ii in range(n):
        for jj in range(n):
            if not visited[ii][jj]:
                bfs(visited, ii, jj)
    if move_list:
        move()
        count += 1
    temp += 1
    if temp != count:
        break


print(count)
