# 두 수의 합
# 정수 수열 안에서 수열의 원소 두 개의 합이 target값이 되는 경우를 찾고 싶습니다.
# 매개변수 nums에 길이가 n인 수열이 주어지고, 매개변수 target에 자연수 값이 주어지면 이
# 수열안에서 두 개의 원소의 합이 정수 target값이 되는 두 원소를 구해 배열에 오름차순으로
# 담아 반환합니다.
# 두 개의 원소의 합이 target값이 되는 경우는 오직 한가지 뿐인 입력만 주어집니다. 한 원소를
# 두 번 더하는 것은 안됩니다. nums의 각 원소는 유일값입니다.
# 답이 없을 경우 [0, 0]을 반환합니다.

# 제한사항:
# • nums의 길이 3 <= n <= 200,000
# **** 시간복잡도 고려 -> 200,000은 O(n)을 고려해야하므로, for문이 한번만 돌아야함
# • 배열 nums의 원소는 정수입니다. -10,000 <= nums[i] <= 10,000
# • -20,000 <= target <= 20,000

# 완전탐색(중첩 반복문 사용필수) -> 모두 짝궁이 되는지 확인
# 상태트리로 표현
from collections import defaultdict

def solutions(nums, target):
    answer = [0]*2
    nH = defaultdict(int) # 해쉬생성

    for x in nums:
            y = target - x
            if y in nH:
                return sorted([x,y])
            nH[x] = 1 # 값이 0으로 기본설정된 딕셔너리(값을 아무것도 없이는 불가)

    return answer

print(solutions([7,3,2,13,9,15,8,11],12))