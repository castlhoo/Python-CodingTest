# 격자판 최대합
# 5*5 격자판에 아래롸 같이 숫자가 적혀있습니다.
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
# N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합
# 니다.

# ▣ 입력설명
# 첫 줄에 자연수 N이 주어진다.(1<=N<=50)
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는
# 다.
# ▣ 출력설명
# 최대합을 출력합니다.
# ▣ 입력예제 1
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
# ▣ 출력예제 1
# 155
n = int(input())
box = list(map(int, input().split()))

max_sum = float('-inf')

for i in range(n):
    sum_1 = sum_2 = 0
    for j in range(n):
        sum_1 += box[i][j]
        sum_2 += box[j][i]
    if sum_1 > max_sum:
         max_sum = sum_1
    if sum_2 > max_sum:
         max_sum = sum_2  

sum_1 = sum_2 = 0
for h in range(n):
    sum_1 += box[h][h]
    resum_1 += box[h][n-1-h]
if sum_1 > max_sum:
        max_sum = sum_1
if sum_2 > max_sum:
        max_sum = sum_2  

print(max_sum)