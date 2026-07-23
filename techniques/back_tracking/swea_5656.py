T = int(input())

def process_brick_boom(y, x, matrix, amount):
    h = len(matrix)
    w = len(matrix[0])

    matrix[y][x] = 0
    if amount == 1:
        return

    for i in range(1, amount):
        if y-i >= 0 and y-i < h: # 인덱스 방어
            process_brick_boom(y-i, x, matrix, matrix[y-i][x]) # 연쇄 반응 처리
        if y+i >= 0 and y+i < h:
            process_brick_boom(y+i, x, matrix, matrix[y+i][x])
        if x-i >= 0 and x-i < w:
            process_brick_boom(y, x-i, matrix, matrix[y][x-i])
        if x+i >= 0 and x+i < w:
            process_brick_boom(y, x+i, matrix, matrix[y][x+i])

def clean_brick_map(matrix):
    h = len(matrix)
    w = len(matrix[0])

    for x in range(w):
        blank_y = h-1
        for y in range(h-1, -1, -1):
            if matrix[y][x] > 0:
                if y != blank_y:
                    matrix[blank_y][x] = matrix[y][x]
                    matrix[y][x] = 0
                blank_y -= 1

for test_case in range(1, T + 1):
    n, w, h = map(int, input().split())
    brick_map = [list(map(int, input().split())) for _ in range(h)]
            
    brick_count = 0
    least_rest_bricks = 99999999
    # 4. 완전 탐색(DFS)으로 반복 -> 모든 경우의 수에 대해서 남은 벽돌 개수 산출
    def dfs(current_brick_map, brick_count):
        global least_rest_bricks

        if brick_count == n:
            local_minimum = 0
            for i in range(h):
                for j in range(w):
                    if current_brick_map[i][j] > 0:
                        local_minimum += 1

            if least_rest_bricks > local_minimum: least_rest_bricks = local_minimum
            return 

    # 1. 깨질 벽돌을 맨 위의 벽돌에서 선택
        for select_column in range(w):
            next_brick_map = [row[:] for row in current_brick_map]

            select_brick_num = 0
            select_row = 0

            for i in range(h):
                if next_brick_map[i][select_column] != 0:
                    select_row = i
                    select_brick_num = next_brick_map[i][select_column]
                    break

            # 2. 선택된 벽돌 제거 작업
            process_brick_boom(select_row, select_column, next_brick_map, select_brick_num)

            # 3. 벽돌 맵 정리
            clean_brick_map(next_brick_map)

            dfs(next_brick_map, brick_count + 1)

    dfs(brick_map, 0)
    print(f"#{test_case} {least_rest_bricks}")


    
        


    

    

    

