# RE
# 연속된 '1'의 길이
# 매개변수 nums에 0과 1로된 수열이 주어지면 
# 1이 연속된 부분수열 중 가장 긴 부분수열의 
# 길이를 반환하는 프로그램을 작성하세요.

# 제한사항:
# • score의 길이 3 <= n <= 100,000
def solutions(nums):
    cnt = 0 
    answer = 0

    for i in nums:
        if i == 1:
            cnt += 1
        else:
            answer = max(answer, cnt)
            cnt = 0
    
    answer = max(answer, cnt)
    return answer
            

print(solutions([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))
print(solutions([0, 0, 1, 0, 1, 0, 0]))
print(solutions([1, 1, 1, 1, 1]))
print(solutions([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]))