# 곳감(모래시계)
# 현수는 곳감을 만들기 위해 감을 깍아 마당에 말리고 있습니다. 현수의 마당은 N*N 격자판으
# 로 이루어져 있으며, 현수는 각 격자단위로 말리는 감의 수를 정합니다.
# 그런데 해의 위치에 따라 특정위치의 감은 잘 마르지 않습니다. 그래서 현수는 격자의 행을
# 기준으로 왼쪽, 또는 오른쪽으로 회전시켜 위치를 변경해 모든 감이 잘 마르게 합니다.
# 만약 회전명령 정보가 2 0 3이면 2번째 행을 왼쪽으로 3만큼 아래 그림처럼 회전시키는 명령
# 입니다.
# 1행 10 13 10 12 15
# 2행 12 39 30 23 11
# 3행 11 25 50 53 15
# 4행 19 27 29 37 27
# 5행 19 13 30 13 19
# 10 13 10 12 15
# 23 11 12 39 30
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
# 첫 번째 수는 행번호, 두 번째 수는 방향인데 0이면 왼쪽, 1이면 오른쪽이고, 세 번째 수는 회
# 전하는 격자의 수입니다.
# M개의 회전명령을 실행하고 난 후 아래와 같이 마당의 모래시계 모양의 영역에는 감 이 총 몇
# 개가 있는지 출력하는 프로그램을 작성하세요.
# 10 13 10 12 15
# 23 11 12 39 30
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
# ▣ 입력설명
# 첫 줄에 자연수 N(3<=N<=20) 이 주어며, N은 홀수입니다.
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
# 이 자연수는 각 격자안에 있는 감의 개수이며, 각 격자안의 감의 개수는 100을 넘지 않는다.
# 그 다음 줄에 회전명령의 개수인 M(1<=M<=10)이 주어지고, 그 다음 줄부터 M개의 회전명령
# 정보가 M줄에 걸쳐 주어집니다.

n = int(input())
box = []
for x in range(n):
    box.append(list(map(int, input().split())))
m = int(input())
for _ in range(m):
    row_num, direction, rotate_count = map(int, input().split())
    row_idx = row_num - 1

    if direction == 0:
        for _ in range(rotate_count):
            box[row_idx].append(box[row_idx].pop(0))
    else:
        for _ in range(rotate_count):
            box[row_idx].insert(0, box[row_idx].pop())

result= []
center = n // 2

for i in range(n):
    dis_center = abs(i-center)
    s_col = center - dis_center
    e_col = center + dis_center

    for j in range(s_col, e_col+1):
        result.append(box[i][j])

print(sum(result))