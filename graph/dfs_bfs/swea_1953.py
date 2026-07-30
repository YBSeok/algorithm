from collections import defaultdict

T = int(input())

# 상, 하, 좌, 우
dy=[-1, 1, 0, 0]
dx=[0, 0, -1, 1]

# 상, 하, 좌, 우의 가능 여부 저장
directions = defaultdict(list)
directions[1] = [1, 1, 1, 1]
directions[2] = [1, 1, 0, 0]
directions[3] = [0, 0, 1, 1]
directions[4] = [1, 0, 0, 1]
directions[5] = [0, 1, 0, 1]
directions[6] = [0, 1, 1, 0]
directions[7] = [1, 0, 1, 0]

def checkCanReceive(curr_direction, next_way_list):
    # 상, 하, 좌, 우
    if curr_direction == 0 and next_way_list[1] == 1:
        return True
    if curr_direction == 1 and next_way_list[0] == 1:
        return True
    if curr_direction == 2 and next_way_list[3] == 1:
        return True
    if curr_direction == 3 and next_way_list[2] == 1:
        return True
    return False


for test_case in range(1, T + 1):
    h, w, y_start, x_start, hours = map(int, input().split())

    escape_map = [[] for _ in range(h)]
    for i in range(h):
        escape_map[i] = list(map(int, input().split()))

    
    reachable = [[0]*w for _ in range(h)]
    def dfs(y, x, curr_dist, visited):
        if curr_dist > hours:
            return
    
        direction = escape_map[y][x]

        if direction == 0:
            return

        visited[y][x] = 1
        reachable[y][x] = 1

        for i in range(4):
            if directions[direction][i] == 1:
                next_y = y + dy[i]
                next_x = x + dx[i]

                # 인덱스 방어
                if 0 <= next_y and next_y < h and 0 <= next_x and next_x < w:
                    if escape_map[next_y][next_x] != 0:
                        if checkCanReceive(i, directions[escape_map[next_y][next_x]]):
                            if visited[next_y][next_x] == 0:
                                dfs(next_y, next_x, curr_dist + 1, visited)


        visited[y][x] = 0

    visited = [[0]*w for _ in range(h)]
    dfs(y_start, x_start, 1, visited)

    result = 0
    for i in range(h):
        for j in range(w):
            if reachable[i][j] == 1:
                result += 1

    print(f"#{test_case} {result}")