# RE
# 합격생
# 코딩테스트 자격증 시험에 합격한 수험생 수를 구하려고 합니다.
# 매개변수 score에 시험을 친 수험생들의 시험 점수가 주어지고, 
# 매개변수 k에 합격 커트라인 점수가 주어지면 
# 자격증 시험에 합격한 수험생의 수를 구해 반환하는 프로그램을 작성하세요.

# 제한사항:
# • score의 길이 3 <= n <= 10,000
# • 0 <= score[i] <= 100
# • 50 <= k <= 90

def solutions(score, k):
    answer = 0
    n = len(score)

    for i in range(n):
        if score[i] >= k:
            answer += 1
    return answer    

print(solutions([60, 50, 80, 90, 55, 70, 65, 45], 60))
print(solutions([10, 20, 30, 40, 50], 60))
print(solutions([50, 65, 75, 87, 90, 55, 78, 93, 100], 70))
print(solutions([99, 30, 50, 55, 68, 70, 90, 100], 80))