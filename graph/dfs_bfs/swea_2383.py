from collections import deque

T = int(input())

# def simulation(choose_stairs):
#     time = 0
#     stair_0_queue = deque()
#     stair_1_queue = deque()

#     while(choose_stairs or stair_0_queue or stair_1_queue):
#         time += 1
#         for i in range(len(choose_stairs)):
#             if stair_0_queue:
#                 stair_0_queue.popleft()
#             if stair_1_queue:
#                 stair_1_queue.popleft()

#             if choose_stairs[i][1] > 0:
#                 choose_stairs[i][1] -= 1

#             next_stairs = choose_stairs[:]
#             if(next_stairs[i][0] == 0):
#                 if next_stairs[i][0] == 0:
#                     stair_0_queue.append(i)
#                 else:
#                     stair_1_queue.append(i)
#                 del next_stairs[i]
#             choose_stairs = next_stairs[:]
            
#     return time

def simulation(choose_stairs, stairs):
    stair_arrivals = [[], []]
    for stair_idx, arrival_time in choose_stairs:
        stair_arrivals[stair_idx].append(arrival_time)
    
    stair_arrivals[0].sort()
    stair_arrivals[1].sort()
    
    max_time = 0
    
    for i in range(2):
        if not stair_arrivals[i]:
            continue
            
        stair_len = stairs[i][2]
        q = deque()
        last_person_time = 0
        
        for arrival in stair_arrivals[i]:
            start_time = arrival + 1 
            
            if len(q) == 3:
                start_time = max(start_time, q.popleft())
                
            finish_time = start_time + stair_len
            q.append(finish_time)
            last_person_time = finish_time
            
        if last_person_time > max_time:
            max_time = last_person_time
            
    return max_time

for test_case in range(1, T + 1):
    n = int(input())
    matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        matrix[i] = list(map(int, input().split()))

    # 거리 집합 계산
    # 계단 수 == 각 인원의 선택지 수, 반드시 2개 라는 조건. 2^10이 최대 가짓수.
    people_count = 0
    stairs = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > 1:
                stairs.append([i,j,matrix[i][j]])
            if matrix[i][j] == 1:
                people_count += 1

    # 각 인원마다 계단까지의 거리 구하기
    dist = []
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == 1:
                person_dist = []
                for stair in stairs:
                    person_dist.append(abs(r - stair[0]) + abs(c - stair[1]))
                dist.append(person_dist)

    # 계산 조합 전체 순회
    result = 99999999999
    def dfs(choose_stairs):
        global result

        if len(choose_stairs) == people_count:
            # 총 소요시간 계산
            temp = simulation(choose_stairs, stairs)
            if result > temp:
                result = temp
            return 

        curr_person = len(choose_stairs)

        for i in range(2):
            choose_stairs.append([i, dist[curr_person][i]])
            dfs(choose_stairs)
            choose_stairs.pop()

    dfs([])
    print(f"#{test_case} {result}")