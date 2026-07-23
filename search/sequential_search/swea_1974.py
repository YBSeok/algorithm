def validate_square(array, width):
    sum_square = 0
    for i in range(width):
        for j in range(width):
            sum_square += array[i][j]
    if sum_square != 45:
        return False
    
    return True

T = int(input())    

for test_case in range(1, T + 1):
    sudoku = [[] for x in range(9)]
    for i in range(9):
        sudoku[i] = list(map(int ,input().split()))

    isPassed = True
    # 직선 검증
    for i in range(9):
        sum_x = 0
        sum_y = 0
        for j in range(9):
            sum_x += sudoku[i][j]
            sum_y += sudoku[j][i]
        if sum_x != 45 or sum_y != 45:
            isPassed = False
            break

    if isPassed:
        for i in range(9):
            for j in range(9):
                if i % 3 == 0 and j % 3 == 0:
                    window = [[] for _ in range(3)]
                    for k in range(3):
                        window[k] = sudoku[i+k][j:j+3]

                    if not validate_square(window, 3):
                        isPassed = False
                        break

    print(f"#{test_case} {1 if isPassed else 0}")