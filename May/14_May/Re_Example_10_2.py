# 검정색 영역구하기
# 5 * 5 이차원 배열에 모니터 화면을 표현합니다. 
# 모니터의 화변은 최초 검정색과 흰색으로만 표현되어 있습니다. 
# 검정색은 1, 흰색은 0으로 표현됩니다.
# 상하좌우로 1(검정색)이 연결되어 있으면 한 영역으로 간주합니다.
# 화면의 격자 정보가 위와 같다면 검정색으로 칠해진 영역은 2곳입니다.
# 매개변수 board에 모니터 화면의 격자정보가 주어지면 
# 검정색으로 칠해진 영역은 총 몇 개가 있는지 구하여 반환하는 프로그램을 작성하세요.
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def BFS(x,y,board):
    Q = deque()
    Q.append([x,y])

    board[x,y] == 0

    L = 0

    while Q:
        n = len(Q)
        for i in range(n):
            x,y = Q.popleft()
    
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx>=0 and nx<5 and ny>=0 and ny<5 and board[nx,ny] == 1:
                Q.append(board[nx,ny])
                board[nx,ny] = 0
        L += 1



def solutions(board):
    answer = 0

    for i in range(5):
        for j in range(5):
            if board[i,j] == 1:
                answer += 1
                BFS(i,j,board)
    return answer