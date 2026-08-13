T = int(input())

def checkTurn(start, turn_list, wheels):
    for i in range(start, 4):
        if turn_list[i] != 0:
            if wheels[i][2] != wheels[i+1][6]:
                turn_list[i+1] = turn_list[i] * -1

    for i in range(start, 1, -1):
        if turn_list[i] != 0:
            if wheels[i][6] != wheels[i-1][2]:
                turn_list[i-1] = turn_list[i] * -1


def turns(wheels, wheel_num, direction):
    # 시계방향
    if direction == 1:
        wheels[wheel_num].insert(0,wheels[wheel_num][7])
        wheels[wheel_num].pop()
    # 반시계방향
    else:
        wheels[wheel_num].append(wheels[wheel_num][0])
        wheels[wheel_num].pop(0)


for test_case in range(1, T + 1):
    k = int(input())
    wheels = []

    wheels.append([])
    for i in range(4):
        arr = list(map(int, input().split()))
        wheels.append(arr)

    for i in range(k):
        wheel_num, direction = map(int, input().split())

        # 돌아갈 때는 바퀴가 한번에 돌아가야함.
        turn_list = [0, 0, 0, 0, 0]
        turn_list[wheel_num] = direction
        checkTurn(wheel_num, turn_list, wheels)

        for i in range(4):
            if turn_list[i+1] != 0:
                turns(wheels, i+1, turn_list[i+1])

    result = 0
    for i in range(4):
            if wheels[i+1][0] == 1:
                result += (1 << i)
    print(f"#{test_case} {result}")