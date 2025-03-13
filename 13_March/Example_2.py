# 제한사항:
# • score의 길이 3 <= n <= 10,000
# • 0 <= score[i] <= 100
# • 50 <= k <= 90
def passexam(score, k):
    answer = 0
    
    for x in score:
        if x >= k:
            answer += 1
    return answer

print(passexam([60,50,80,90,55,70,65,45], 60))
print(passexam([50,65,75,87,90,55,78,93,100], 70))