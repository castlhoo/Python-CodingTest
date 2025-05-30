# 검정색 영역구하기
# 5 * 5 이차원 배열에 모니터 화면을 표현합니다. 
# 모니터의 화변은 최초 검정색과 흰색으로만 표현되어 있습니다. 
# 검정색은 1, 흰색은 0으로 표현됩니다.
# 상하좌우로 1(검정색)이 연결되어 있으면 한 영역으로 간주합니다.
# 화면의 격자 정보가 위와 같다면 검정색으로 칠해진 영역은 2곳입니다.
# 매개변수 board에 모니터 화면의 격자정보가 주어지면 
# 검정색으로 칠해진 영역은 총 몇 개가 있는지 구하여 반환하는 프로그램을 작성하세요.

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def DFS(x,y,board):
    board[x][y] = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx>=0 and nx<5 and ny>=0 and ny<5 and board[nx][ny]==1:
            DFS(nx, ny, board)


def solutoins(board):
    answer = 0
    n = len(board)

    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:
                answer += 1
                DFS(i,j,board)
    return answer

print(solutoins([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0,
1, 0], [0, 0, 1, 1, 0]]))
print(solutoins([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0,
1, 0], [1, 0, 1, 0, 0]]))
print(solutoins([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0,
1, 0], [0, 0, 1, 1, 0]]))
print(solutoins([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0,
1, 0], [0, 0, 1, 0, 0]]))