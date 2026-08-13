T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
        
    # 복도는 총 400개의 방을 마주보며 200개의 구간으로 나뉨
    corridor = [0] * 201 
        
    for _ in range(n):
        start, end = map(int, input().split())
            
        # 출발지가 목적지보다 번호가 큰 경우(역방향 이동) 스왑
        if start > end:
            start, end = end, start
            
        # 방 번호를 복도 인덱스(1~200)로 변환
        s_idx = (start + 1) // 2
        e_idx = (end + 1) // 2
            
        # 이동하는 복도 구간에 1씩 누적
        for i in range(s_idx, e_idx + 1):
            corridor[i] += 1
                
    # 복도 구간 중 가장 많이 겹친 횟수가 정답 (단위 시간)
    result = max(corridor)
    print(f"#{test_case} {result}")
