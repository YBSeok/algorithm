# 어떤 바위를 제거할 지 찾자!
# def solution(distance, rocks, n):
#         result = -99999999
    
#     for curr_combination in combinations(rocks, n): # O(조합 개수)
        
#         ## 조합 삭제
#         rocks_copied = rocks[:]
#         for rock in rocks:  # O(n)
#             if rock in curr_combination:
#                 rocks_copied.remove(rock)  # O(n)
        
#         ## 거리 재계산
#         new_distance = []
#         rocks_copied.sort() # O(nlogn)
        
#         new_distance.append(rocks_copied[0])
#         for i in range(len(rocks_copied) - 1): # O(n)
#             new_distance.append(rocks_copied[i+1] - rocks_copied[i])
#         new_distance.append(distance - sum(new_distance))
        
#         local_result = min(new_distance)
#         if result < local_result:
#             result = local_result
        
#     return result

# 어떤 바위를 제거할 지 찾지말고 질문을 바꾸자.
# 기존 질문: 어떤 바위를 제거해야 최소 거리가 최대가 될까?
# 새로운 질문: 최소 거리를 10으로 만들고 싶다. 그러면 바위를 몇 개 제거해야 할까?
def solution(distance, rocks, n):
    answer = 0
    # 해당 값이 최솟값이 가능한지 여부를 체크
    rocks.sort()
    def check(mid):
        count = 0
        prev = 0

        for rock in rocks:
            if rock - prev < mid:
                count += 1
            else:
                prev = rock

        if distance - prev < mid:
            count += 1

        return count <= n
    
    # 0 ~ distance
    left = 0
    right = distance
    while left <= right:
        mid = (left+right) // 2
        
        if check(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
        
    return answer