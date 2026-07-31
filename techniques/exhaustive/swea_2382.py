T = int(input())

dy=[0, -1, 1, 0, 0]
dx=[0, 0, 0, -1, 1]
opposite=[0, 2, 1, 4, 3]

def remove(y, x, matrix):
    matrix[y][x][0] = 0
    matrix[y][x][1] = 0
    matrix[y][x][2] = 0

def crushBorder(y, x, matrix):
    matrix[y][x][0] = int(matrix[y][x][0]/2)
    matrix[y][x][1] = opposite[matrix[y][x][1]]

def move(y, x, matrix, width):
    direction = matrix[y][x][1]
    ny = y + dy[direction]
    nx = x + dx[direction]
    if 0 <= ny and ny < width and 0 <= nx and nx < width:        
        if matrix[ny][nx][0] == 0: # simple move
            matrix[ny][nx][0] = matrix[y][x][0]
            matrix[ny][nx][1] = matrix[y][x][1]

        else: # merge
            matrix[ny][nx][0] += matrix[y][x][0]
            if matrix[ny][nx][0] < matrix[y][x][0]:
                matrix[ny][nx][1] = matrix[y][x][1]

        if ny == 0 or ny == width-1 or nx == 0 or nx == width-1:
            crushBorder(ny, nx, matrix)

        if matrix[ny][nx][0] == 0:
            remove(ny, nx, matrix)

        remove(y, x, matrix)

    return

for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())

    matrix = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
    
    for i in range(k):
        y, x, count, direction = map(int, input().split())
        matrix[y][x][0] = count
        matrix[y][x][1] = direction

    for i in range(m):

        for j in range(n):
            for k in range(n):
                if matrix[j][k][0] != 0:
                    matrix[j][k][2] = 1 # 이동 가능 거리 부여

        for j in range(n):
            for k in range(n):
                if matrix[j][k][0] != 0 and matrix[j][k][2] == 1:
                    move(j, k, matrix, n)

    result = 0
    for i in range(n):
        for j in range(n):
            result += matrix[i][j][0]

    print(f"#{test_case} {result}")