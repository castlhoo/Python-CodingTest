# 청소 로봇(ver 1)
# 이차원 배열 격자판 0행 0열이 청소 로봇의 시작위치입니다.\

# 청소 로봇은 다음 규칙에 따라 이동합니다.
# 1. 'U' 명령은 로봇이 위쪽으로 한 칸 이동합니다.
# 2. 'R' 명령은 로봇이 오른쪽으로 한 칸 이동합니다.
# 3. 'L' 명령은 로봇이 왼쪽으로 한 칸 이동합니다.
# 4. 'D' 명령은 로봇이 아래쪽으로 한 칸 이동합니다.
# 매개변수 moves에 청소 로봇에 명령을 내린 문자들이 
# 차례대로 나열된 명령 문자열이 주어지면 
# 이 명령 문자열을 청소 로봇이 모두 수행했을 때 
# 최종 위치를 반환하는 프로그램을 작성하세요. 
# 격자판 밖으로 벗어나는 명령은 주어지지 않습니다.

# 제한사항:
# • moves의 길이는 100을 넘지 않습니다.
# • 2차원 배열 격자판의 크기는 100*100입니다.

def solutions(moves):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    x = 0
    y = 0

    for i in moves:
        if i == "U":
            x = x + dx[0]
            y = y + dy[0]
        elif i == "R":
            x = x + dx[1]
            y = y + dy[1]
        elif i == "D":
            x = x + dx[2]
            y = y + dy[2]
        elif i == "L":
            x = x + dx[3]
            y = y + dy[3]
    
    return [x, y]

print(solutions("RRRDDDLU"))
print(solutions("DDDRRRDDLL"))
print(solutions("RRRRRRDDDDDDUULL"))
print(solutions("RRRRDDDRRDDLLUU"))