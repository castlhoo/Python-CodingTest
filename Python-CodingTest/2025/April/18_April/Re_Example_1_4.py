# RE
# 수열의 회전
# 정수 수열의 원소를 회전하고 싶습니다.
# 매개변수 nums에 길이가 n인 수열이 주어지고, 
# 매개변수 k에 뒤로 이동시키고 싶은 원소의 개수가 주어지면 
# nums의 원소 중 앞 원소 k개를 수열의 뒤쪽으로 이동하고 난 후의 
# 수열을 반환하는 프로그램을 작성하세요.

# 제한사항:
# • nums의 길이 3 <= n <= 200,000
# • 배열 nums의 원소는 정수입니다. -10,000 <= nums[i] <= 10,000
# • 0 <= k <= nums의 길이
from collections import deque

def solutions(nums, k):
    answer = deque(nums)

    for i in range(k):
        answer.append(answer.popleft())
    return answer
        
print(solutions([3, 7, 1, 5, 9, 2, 8], 3))
print(solutions([2, 12, 2, 1, 3, 3, 9], 2))
print(solutions([1, 2, 5, 4, 6, 7, 9], 6))
print(solutions([1, 3, 6, 8, 14, 2, 1, 7], 5))