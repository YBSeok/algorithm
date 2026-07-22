#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    curr_case = str(input())
    curr_case_lenght = len(curr_case)
    expire_count = 0
    
    curr_clapper = 0
    for i in range(curr_case_lenght):
        curr_clapper += int(curr_case[i])

        while(curr_clapper <= i):
            expire_count += 1
            curr_clapper += 1
            
    print('#' + str(test_case) + ' ' + str(expire_count))
    # ///////////////////////////////////////////////////////////////////////////////////