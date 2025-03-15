# 매개변수 nums에 길이가 n인 수열이 주어지면 수열의 원소중에서 빈도수가 1인 가장 큰 숫자
# 를 반환하는 프로그램을 작성하세요. 빈도수 1인 숫자가 없을 경우 -1를 반환하세요.

# 제한사항:
# • nums의 길이 3 <= n <= 10,000
# • 배열 nums의 원소는 자연수입니다. 1 <= nums[i] <= 1,000,000,000
from collections import defaultdict # 빈도수 카운팅
def solution(nums):
    answer = -1 # 빈도수가 1인 숫자가 없을때를 기본값으로 설정
    nH = defaultdict(int) # value 타입 지정 (키값이 존재하지 않으면 벨류는 0) 
    # nH = Counter(nums) # nums의 빈도수 카운팅하는 함수 (Counter import해야함)

    for x in nums:
        nH[x] += 1 # 키의 벨류값 1씩 증가
    for key in nH:
        if nH[key] == 1:
            answer = max(answer, key)

    return answer


print(solution([3,9,2,12,9,12,8,7,9,12]))
print(solution([2,1,3,2,1,3,4,5,4,5,6,7,6,7,8,8]))

