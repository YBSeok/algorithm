T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for test_case in range(1, T + 1):
    n, k = map(int, input().split())

    matrix = [[] for _ in range(n)]
    for i in range(n):
        matrix[i] = list(map(int, input().split()))

    result = 0
    def dfs(y, x, dist, visited, isDigged):
        global result
        result = max(result, dist)

        visited[y][x] = 1
        
        for i in range(4):
            next_y = y + dy[i]
            next_x = x + dx[i]
            
            if 0 <= next_y < n and 0 <= next_x < n:
                if visited[next_y][next_x] == 0:
                    temp = 0
                    if matrix[next_y][next_x] < matrix[y][x]:        
                        dfs(next_y, next_x, dist+1, visited, isDigged)
                    elif not isDigged and matrix[next_y][next_x] - k < matrix[y][x]:
                        temp = matrix[next_y][next_x]
                        matrix[next_y][next_x] = matrix[y][x] - 1
                        dfs(next_y, next_x,  dist+1, visited, True)
                        matrix[next_y][next_x] = temp
        visited[y][x] = 0
                    
    # 각 셀마다 최대 경로 수 파악
    max_h = max(map(max, matrix))

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == max_h:
                visited = [[0]*n for _ in range(n)]
                dfs(i,j, 1, visited, 0)


    print(f"#{test_case} {result}")