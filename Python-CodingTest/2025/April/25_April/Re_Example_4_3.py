# 청소 로봇(ver 2)
# 이차원 배열 격자판 0행 0열이 청소 로봇의 시작위치입니다.\

# 청소 로봇은 다음 규칙에 따라 이동합니다.
# 1. 'U' 명령은 로봇이 위쪽으로 한 칸 이동합니다.
# 2. 'R' 명령은 로봇이 오른쪽으로 한 칸 이동합니다.
# 3. 'L' 명령은 로봇이 왼쪽으로 한 칸 이동합니다.
# 4. 'D' 명령은 로봇이 아래쪽으로 한 칸 이동합니다.
# 5. 만약 로봇이 명령을 수행할 경우 격자판 밖으로 나가는 경우라면 
# 로봇은 해당 명령을 수행하지 않고 무시합니다.

# 매개변수 n에 격자판 크기가 주어지고, moves에 청소 로봇에 명령을 내린 문자들이 차례대로
# 나열된 명령 문자열이 주어지면 청소 로봇이 최종적으로 멈춘 위치를 반환하는 프로그램을 작
# 성하세요.

# 제한사항:
# • moves의 길이는 100을 넘지 않습니다.
# • 3 <= n <= 50

def solutions(n, moves):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    loc = ['U', 'R', 'D', 'L']

    x = 0
    y = 0

    for i in moves:
        for j in range(4):
            if i == loc[j]:
                nx = x + dx[j]
                ny = y + dy[j]
        
        if nx >= n and nx < 0 and ny >= n and ny < 0:
            continue

        x = nx
        y = ny

    return [x, y]

print(solutions(5, "RRRDDDLU"))
print(solutions(7, "DDDRRRDDLL"))
print(solutions(5, "RRRRRRDDDDDDUULL"))
print(solutions(6, "RRRRDDDRRDDLLUU"))