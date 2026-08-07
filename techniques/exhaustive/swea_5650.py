def solve():
    T = int(input())
    
    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)

    change = (
        (),
        (1, 3, 0, 2),   # block1
        (3, 0, 1, 2),   # block2
        (2, 0, 3, 1),   # block3
        (1, 2, 3, 0),   # block4
        (1, 0, 3, 2),   # block5 (벽 포함)
    )

    for tc in range(1, T + 1):
        N = int(input())
        board = [list(map(int, input().split())) for _ in range(N)]

        wormholes = [[] for _ in range(11)]
        zeros = []
        
        for i in range(N):
            for j in range(N):
                v = board[i][j]
                if v == 0:
                    zeros.append((i, j))
                elif v >= 6:
                    wormholes[v].append((i, j))

        ans = 0
        
        for sy, sx in zeros:
            for sd in range(4):
                y, x, d = sy, sx, sd
                score = 0

                # 시뮬레이션 시작
                while True:
                    y += dy[d]
                    x += dx[d]

                    # 1. 벽
                    if not (0 <= y < N and 0 <= x < N):
                        d = change[5][d]
                        score += 1
                        continue

                    # 2. 종료 조건 (출발점으로 복귀)
                    if y == sy and x == sx:
                        if score > ans: 
                            ans = score
                        break

                    v = board[y][x]

                    # 3. 빈 공간
                    if v == 0:
                        continue
                        
                    # 4. 블랙홀
                    if v == -1:
                        if score > ans:
                            ans = score
                        break

                    # 5. 블록 1~5
                    if v <= 5:
                        d = change[v][d]
                        score += 1
                        
                    # 6. 웜홀 6~10
                    else:
                        w1, w2 = wormholes[v]
                        if w1[0] == y and w1[1] == x:
                            y, x = w2
                        else:
                            y, x = w1

        print(f"#{tc} {ans}")

if __name__ == '__main__':
    solve()