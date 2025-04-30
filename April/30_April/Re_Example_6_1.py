# 버스
# 학생들이 버스에 타고 여행을 가려고 합니다.
# 버스는 승객을 태울 수 있는 무게 제한이 있습니다.
# 매개변수 weight에 각 학생들의 몸무게 정보가 주어지고, 
# limit에 버스가 태울 수 있는 총 승객의 무게가 주어지면 
# 버스에 탈 수 있는 최대인원수를 구하여 반환하는 프로그램을 작성하세요.

# 제한사항:
# • weight의 길이는 100,000을 넘지 않습니다.
# • 50 <= weight[i] <= 300
# • 100 <= limit <= 100,000,000

def solutions(weight, limit):
    weight.sort()
    n = len(weight)
    tem = 0
    answer = 0

    for i in range(n):
        if tem + weight[i] > limit:
            break
        tem += weight[i]
        answer += 1

    return answer

print(solutions([300, 100, 230, 120, 90, 150, 60], 700))
print(solutions([50, 90, 70, 120, 300, 200, 150, 180, 190], 1000))
print(solutions([70, 90, 100, 80, 60, 75, 73, 85, 120, 110, 200], 800))
print(solutions([50, 90, 100, 130, 140, 120, 130, 120, 150, 160, 140,
170], 1000))
print(solutions([100, 110, 50, 50, 60, 70, 50, 55, 57] ,350))