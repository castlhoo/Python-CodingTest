# 제한사항:
# • nums의 길이 3 <= n <= 200,000 *** 100,000 이상이면 효율성 생각해야함
# • 배열 nums의 원소는 정수입니다. -10,000 <= nums[i] <= 10,000
# • 0 <= k <= nums의 길이

from collections import deque
def solution(nums, k):
    answer = deque(nums)

    for i in range(k):
        answer.append(answer.popleft())
    return list(answer)

print(solution([3,7,1,5,9,2,8],3))
print(solution([2,12,2,1,3,3,9],2))
print(solution([1,3,6,8,14,2,1,7],5))

# 배열이므로 pop() 하면 O(n)으로 하면 시간복잡도 안좋음
# deque로 변경해서 해결 -> O(1) 시간복잡도
# 배열로 반환하라고 했으니까 list 변환 필수

