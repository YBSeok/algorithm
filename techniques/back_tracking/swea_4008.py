T = int(input())

def caculate(operator, operand_1, operand_2):
    if operator == 0:
        return operand_1 + operand_2
    elif operator == 1:
        return operand_1 - operand_2
    elif operator == 2:
        return operand_1 * operand_2
    elif operator == 3:
        if operand_1 < 0 or operand_2 < 0:
            return - (abs(operand_1) // abs(operand_2))
        return operand_1 // operand_2

for test_case in range(1, T + 1):
    n = int(input())
    operators = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    
    operate_count = 0
    results = []
    def dfs(rest_operators, curr_num):
        global operate_count
        # 종료조건
        if operate_count == n - 1:
            results.append(curr_num)
            return
        
        # 다음 함수 호출
        for index, operator in enumerate(operators):
            if operator > 0:
                # 현재 상태 계산
                next_num = caculate(index, curr_num, numbers[operate_count+1])

                rest_operators[index] -= 1
                operate_count += 1
                
                dfs(rest_operators, next_num)

                rest_operators[index] += 1
                operate_count -= 1

    dfs(operators, numbers[0])

    print(f"#{test_case} {max(results) - min(results)}")