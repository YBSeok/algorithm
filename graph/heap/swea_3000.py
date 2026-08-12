import heapq
 
T = int(input())
 
for test_case in range(1, T + 1):
    n, first_number = map(int, input().split())
 
    max_heap = []
    min_heap = []
 
    sum = 0
    mid = first_number
    for i in range(n): # o(n)
        new_1, new_2 = map(int, input().split())
         
        if new_1 < mid:
            heapq.heappush(max_heap, -new_1)
        else:
            heapq.heappush(min_heap, new_1)
   
        if new_2 < mid:
            heapq.heappush(max_heap, -new_2)
        else:
            heapq.heappush(min_heap, new_2)
 
        while len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, mid)
            mid = -heapq.heappop(max_heap)
 
        while len(max_heap) < len(min_heap):
            heapq.heappush(max_heap, -mid)
            mid = heapq.heappop(min_heap)
 
        sum += (mid % 20171109)
     
    result = sum % 20171109
    print(f"#{test_case} {result}")