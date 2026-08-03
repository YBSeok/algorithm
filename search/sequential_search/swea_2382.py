T = int(input())

dy=[0, -1, 1, 0, 0]
dx=[0, 0, 0, -1, 1]
opposite=[0, 2, 1, 4, 3]

def crushBorder(y, x, next_matrix):
    next_matrix[y][x][0] = int(next_matrix[y][x][0]/2)
    next_matrix[y][x][1] = opposite[next_matrix[y][x][1]]

def move(y, x, matrix, next_matrix, width):
    direction = matrix[y][x][1]
    ny = y + dy[direction]
    nx = x + dx[direction]
    if 0 <= ny and ny < width and 0 <= nx and nx < width:        
        if next_matrix[ny][nx][0] == 0: # simple move
            next_matrix[ny][nx][0] = matrix[y][x][0]
            next_matrix[ny][nx][1] = matrix[y][x][1]
            next_matrix[ny][nx][2] = matrix[y][x][0]

        else: # merge
            next_matrix[ny][nx][0] += matrix[y][x][0]

            if next_matrix[ny][nx][2] < matrix[y][x][0]:
                next_matrix[ny][nx][1] = matrix[y][x][1]
                next_matrix[ny][nx][2] = matrix[y][x][0]

        if ny == 0 or ny == width-1 or nx == 0 or nx == width-1:
            crushBorder(ny, nx, next_matrix)
    return

for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())

    matrix = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
    
    for i in range(k):
        y, x, count, direction = map(int, input().split())
        matrix[y][x][0] = count
        matrix[y][x][1] = direction

    for i in range(m):

        # 새로운 매트릭스에 저장, 마지막에 갈아낌
        next_matrix = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
        for j in range(n):
            for k in range(n):
                if matrix[j][k][0] != 0:
                    move(j, k, matrix, next_matrix, n)
                    
        matrix = next_matrix

    result = 0
    for i in range(n):
        for j in range(n):
            result += matrix[i][j][0]

    print(f"#{test_case} {result}")