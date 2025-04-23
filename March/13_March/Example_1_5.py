# 제한사항:
# • nums의 길이 3 <= n <= 200,000
# • 배열 nums의 원소는 정수입니다. -10,000 <= nums[i] <= 10,000
from collections import deque

def solution(nums):
    answer = deque()
    answer.appendleft(nums[0])

    for i in range(1, len(nums)):
        if nums[i-1] != nums[i]:
            answer.appendleft(nums[i]) # 왼쪽부터 넣으면서 내림차순 설정
    return list(answer)

print(solution([0,1,1,1,2,2,2,3]))