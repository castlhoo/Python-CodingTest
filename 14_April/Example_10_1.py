# 최소 점프
# 현수는 놀이터에서 놀다가 집으로 가려고 합니다. 
# 놀이터의 위치와 집의 위치가 수직선상의 좌표 점으로 주어집니다. 
# 놀이터는 수직선상의 0지점입니다.
# 현수는 놀이터에서 스카이콩콩을 타고 점프를 하면서 집으로 이동하려고 합니다.
# 점프는 다음과 같은 규칙으로 합니다.
# 1) 현재 지점에서 앞으로 +1 만큼 점프이동할 수 있습니다.
# 2) 현재 지점에서 뒤쪽으로 -1 만큼 점프이동할 수 있습니다.
# 3) 현재 지점에서 앞쪽으로 +5 만큼 긴 점프이동을 할 수있습니다.
# 매개변수 home에 현수의 집의 위치가 주어지면 
# 놀이터에서 집까지 최소 몇 번의 점프로 집에 도착할 수 있는지 
# 최소 점프횟수를 구하여 반환하세요.

# 제한사항:
# • 수직선의 좌표는 0부터 10,000까지입니다.
# • 현수가 집으로 반드시 갈 수 있습니다.
from collections import deque

def BFS(home):
    ch = [0] * 10001
    Q = deque()
    Q.append(0)
    ch[0] = 1
    L = 0

    while Q:
        n = len(Q)
        for i in range(n):
            v = Q.popleft()
            if v == home:
                return L
    
            for nv in [v+1, v-1, v+5]:
                if nv >= 0 and nv < 100000 and ch[nv] == 0 : # check duplication
                    Q.append(nv)
                    ch[nv] = 1
            
        L += 1

def solutions(home):
    answer = BFS(home)
    return answer

print(solutions(10))
print(solutions(14))
print(solutions(25))
print(solutions(24))
print(solutions(345))