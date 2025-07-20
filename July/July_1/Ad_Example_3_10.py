# 스토쿠 검사
# 스도쿠는 매우 간단한 숫자 퍼즐이다. 9×9 크기의 보드가 있을 때, 각 행과 각 열, 그리고 9
# 개의 3×3 크기의 보드에 1부터 9까지의 숫자가 중복 없이 나타나도록 보드를 채우면 된다.
# 예를 들어 다음을 보자.
# 1 4 3 6 2 8 5 7 9
# 5 7 2 1 3 9 4 6 8
# 9 8 6 7 5 4 2 3 1
# 3 9 1 5 4 2 7 8 6
# 4 6 8 9 1 7 3 5 2
# 7 2 5 8 6 3 9 1 4
# 2 3 7 4 8 1 6 9 5
# 6 1 9 2 7 5 8 4 3
# 8 5 4 3 9 6 1 2 7
# 위 그림은 스도쿠를 정확하게 푼 경우이다. 각 행에 1부터 9까지의 숫자가 중복 없이 나오
# 고, 각 열에 1부터 9까지의 숫자가 중복 없이 나오고, 각 3×3짜리 사각형(9개이며, 위에서 색
# 깔로 표시되었다)에 1부터 9까지의 숫자가 중복 없이 나오기 때문이다.
# 완성된 9×9 크기의 수도쿠가 주어지면 정확하게 풀었으면 “YES", 잘 못 풀었으면 ”NO"를 출
# 력하는 프로그램을 작성하세요.
# ▣ 입력설명
# 첫 번째 줄에 완성된 9×9 스도쿠가 주어집니다.
# ▣ 출력설명
# 첫째 줄에 “YES" 또는 ”NO"를 출력하세요.
from collections import Counter

box = []
for x in range(9):
    box.append(list(map(int, input().split())))
is_valied = True

for i in range(9):
    row_counter = Counter(box[i])
    for x in row_counter:
        if row_counter[x] > 1:
            is_valied = False
            break
    if not is_valied:
        break
    
for j in range(9):
    col_counter = Counter(box[k][j] for k in range(9))
    for x in col_counter:
        if col_counter[x] > 1:
            is_valied = False
            break
    if not is_valied:
        break

for box_row in range(3):
    for box_col in range(3):
        box_elements = []
        for i in range(3):
            for j in range(3):
                row = box_row * 3 + i
                col = box_col * 3 + j
                box_elements.append(box[row][col])

        box_counter = Counter(box_elements)
        for x in box_counter:
            if box_counter[x] > 1:
                is_valied = False
                break
        if not is_valied:
            break

if is_valied:
    print("YES")
else:
    print("NO")