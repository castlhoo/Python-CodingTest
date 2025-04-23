# • nums의 길이 3 <= n <= 10,000
# • 배열 nums의 원소는 정수입니다. -10,000 <= nums[i] <= 10,000
# • -20,000 <= target <= 20,000

# O(n^2)
# 완전탐색(중첩 반복문 사용필수) -> 모두 짝궁이 되는지 확인
# 상태트리로 표현
def solutions(nums, target):
    answer = [0] * 2
    n = len(nums)

    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return(nums[i], nums[j])
    return answer

print(solutions([7,3,2,13,9,15,8,11],12))