# 로봇의 이동
# 이차원 배열 격자판 0행 0열에 로봇이 3시 방향을 보고 있습니다.
# 로봇은 다음 규칙에 따라 이동합니다.
# 1. 'G' 명령을 주면 보고 있는 방향으로 한 칸 이동합니다. 
# 격자 밖으로 나가는 명령은 하지
# 않습니다.
# 2. 'R' 명령을 주면 오른쪽으로 90도 회전합니다.
# 3. 'L' 명령을 주면 왼쪽으로 90도 회전합니다.
# 매개변수 moves에 로봇에 명령을 내린 문자들이 
# 차례대로 나열된 명령 문자열이 주어지면 이
# 명령 문자열을 로봇이 모두 수행했을 때 
# 최종 위치를 반환하는 프로그램을 작성하세요

# 제한사항:
# • moves의 길이는 100을 넘지 않습니다.
# • 2차원 배열 격자판의 크기는 100*100입니다.

def solutions(moves):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    d = 1

    x = 0
    y = 0

    for i in moves:
        if i == "G":
            x = x + dx[d]
            y = y + dy[d]
        elif i == "R":
            d = (d+1)%4
        elif i == "L":
            d = (d-1)%4

    return [x, y]

print(solutions("GGGRGGG"))
print(solutions("GGRGGG"))
print(solutions("GGGGGGGRGGGRGGRGGGLGGG"))
print(solutions("GGLLLGLGGG"))    