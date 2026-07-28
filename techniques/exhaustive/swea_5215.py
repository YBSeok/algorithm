T = int(input())

for test_case in range(1, T + 1):
    n, max_calorie = map(int, input().split())

    ingredients = [[] for _ in range(n)]
    
    for i in range(n):
        temp = list(map(int, input().split()))
        ingredients[i].append(temp[0])
        ingredients[i].append(temp[1])

    # 인덱스의 방향과 순회하는 방향이 같으면 아직 갱신하지 않은 값을 만나게 된다.
    dp = [0] * (max_calorie + 1)
    for ingredient in ingredients:
        for i in range(max_calorie, ingredient[1]-1, -1):
            dp[i] = max(dp[i], dp[i-ingredient[1]] + ingredient[0])

    print(f"#{test_case} {dp[max_calorie]}")

    # 브루트 포스
    # ingredients = [[] for _ in range(n)]
    # ingredients_dict = defaultdict(list)
    
    # for i in range(n):
    #     temp = list(map(int, input().split()))
    #     ingredients[i].append(temp[0])
    #     ingredients[i].append(temp[1])
    #     ingredients_dict[i].append(ingredients[i][0])
    #     ingredients_dict[i].append(ingredients[i][1])

    # atLeastOneCombination = True
    # available_prefer = []
    # combination_count = 1
    # while(atLeastOneCombination):
    #     curr_comb = combinations(ingredients_dict.keys(), combination_count)
    #     curr_count = 0

    #     for comb in curr_comb:
    #         total_prefer = 0
    #         total_calorie = 0
    #         for item in comb:
    #             total_prefer += ingredients_dict[item][0]
    #             total_calorie += ingredients_dict[item][1]

    #         if total_calorie <= max_calorie:
    #             available_prefer.append(total_prefer)
    #             curr_count += 1
    #     if curr_count == 0:
    #         atLeastOneCombination = False

    #     combination_count += 1
        
    # result = max(available_prefer)
    # print(f"#{test_case} {result}")
