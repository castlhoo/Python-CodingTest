# 자기 분열수란 배열의 원소 중 자기 자신의 숫자만큼 빈도수를 갖는 숫자를 의미합니다.
# 만약 배열이 [1, 2, 3, 1, 3, 3, 2, 4] 라면
# 1의 빈도수는 2,
# 2의 빈도수는 2,
# 3의 빈도수는 3,
# 4의 빈도수는 1입니다.
# 여기서 자기 자신의 숫자와 같은 빈도수를 갖는 자기 분열수는 2와 3입니다.
# 매개변수 nums에 자연수가 원소인 배열이 주어지면 이 배열에서 자기 분열수 중 가장 작은
# 수를 찾아 반환하는 프로그램을 작성하세요. 자기 분열수가 존재하지 않으면 -1를 반환하세
# 요.

# 제한사항:
# • nums의 길이 3 <= n <= 500,000 -> 효율성 생각!!
# • 배열 nums의 원소는 자연수입니다. 1 <= nums[i] <= 1,000,000
from collections import Counter
def solution(nums):
    answer = 1000000
    nH = Counter(nums)

    for key in nH:
        if key == nH[key]:
            answer = min(answer, key)

    if answer == 100000000:
        return -1
    
    return answer
  
print(solution([1, 2, 3, 1, 3, 3, 2, 4]))