# 제한사항:
# • nums의 길이 3 <= n <= 100,000

def solution(nums):
    answer = 0
    cnt = 0

    for i in nums:
        if i == 1:
            cnt += 1
        else: # 1이 아닌 값을 만나면 갱신
            answer = max(answer, cnt) # 값 비교하여 출력
            cnt = 0 # 연속이 끊기니까 초기화

    answer = max(answer, cnt) # 끝까지 cnt는 커지므로, 마지막 cnt 값과 비교해야함

    return answer

print(solution([1,1,0,1,1,1,0,1,1,1,1,1]))
print(solution([0,0,1,0,1,0,0]))
print(solution([1,1,1,1,1]))


            