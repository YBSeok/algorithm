T = int(input())

for test_case in range(1, T + 1):
    n = int(input())

    matrix = [[] for _ in range(n)]
    for i in range(n):
        matrix[i] = list(map(int, input().split()))

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited = [[0]*n for _ in range(n)]

    curr_max_dist = 0
    def dfs(y, x, curr_dist, visited):
        global curr_max_dist

        if curr_max_dist < curr_dist:
             curr_max_dist = curr_dist

        # 현재 상태 갱신
        visited[y][x] = 1

        for i in range(4):
            # 인덱스 방어
            if 0 <= y + dy[i] and y + dy[i] < n :
                if 0 <= x + dx[i] and x + dx[i] < n :
                    # 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 1 큰지 확인
                    if matrix[y + dy[i]][x + dx[i]] - matrix[y][x] == 1:
                        if visited[y + dy[i]][x + dx[i]] == 0:
                            dfs(y + dy[i], x + dx[i], curr_dist + 1, visited)

        visited[y][x] = 0
            
    max_start = 0
    max_dist = 0
    for i in range(n):
        for j in range(n):
            dfs(i, j, 1, visited)

            if max_dist < curr_max_dist:
                max_dist = curr_max_dist
                max_start = matrix[i][j]

            if max_dist == curr_max_dist:
                if max_start > matrix[i][j]:
                    max_start = matrix[i][j]
            curr_max_dist = 0
            
    print(f"#{test_case} {max_start} {max_dist}")