# 고장난 프린터
# 현수가 다니는 회사의 프린터가 고장이 나서 프린트를 요청한 순서대로 
# 프린트를 하는게 아니라 약간 이상은 규칙에 의해서 프린트를 합니다.
# 이상한 규칙은 다음과 같습니다.
# 요청한 순서에서 먼저 2개의 작업을 프린트하고, 3번째 작업은 순서상 맨 뒤로 보내버립니다.
# 이 규칙을 반복하면서 프린트를 합니다.
# 만약 프린트를 요청한 작업번호 순서가 아래와 같다면
# [3, 1, 4, 5, 2, 6, 7]
# 3번, 1번 작업을 프린트 하고, 4번 작업은 맨뒤로 보냅니다.
# [5, 2, 6, 7, 4]
# 5번, 2번 작업을 프린트 하고, 6번 작업을 맨뒤로 보냅니다.
# [7, 4, 6]
# 7번, 4번 작업을 프린트 하고 6번 작업을 맨뒤로 보냅니다.
# [6]
# 마지막으로 6번 작업을 프린트합니다.
# 매개변수 nums에 프린트를 요청한 작업번호 순서가 주어지면 
# 맨 마지막에 출력되는 작업의 번호를 반환하는 프로그램을 작성하세요.

# 제한사항:
# • nums의 길이는 1,000을 넘지 않습니다.
# • 1 <= nums[i] <= 1,000
from collections import deque

def solutions(nums):
    queue = deque(nums)

    while queue: # when queue is empty, while-program end
        for i in range(2): # repeat twice
            if len(queue) >= 2:
                queue.popleft() # delete first and second values
        queue.append(queue.popleft()) # After deleting, third one moves to the back of the queue
        if len(queue) == 1:
            return queue[0]

print(solutions([3, 1, 4, 5, 2, 6, 7]))
print(solutions([10, 8, 3, 1, 4, 5, 2, 6, 7, 9]))
print(solutions([10, 8, 3, 11, 12, 1, 4, 5, 2, 6, 7, 9]))
print(solutions([10, 8, 3, 1, 4, 5, 2, 11, 13, 6, 7, 12, 9, 14]))
print(solutions([1, 8, 6, 10, 4, 7, 2, 5, 3, 9]))