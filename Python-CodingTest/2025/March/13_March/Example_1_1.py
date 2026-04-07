# 제한사항:
# • nums의 길이 3 <= n <= 100,000 
#       -> 10만이상이면 O(n^2)은 불가 = O(n) or O(nlogn)
# • 배열 nums의 원소는 정수입니다. -1,000,000 <= nums[i] <= 1,000,000
# • 배열 nums의 원소는 중복된 값이 존재하지 않습니다.

# 순차탐색하면서 최소값 찾기 -> O(n)
def solutions(nums):
    answer = 0
    min_number = 100000000
    n = len(nums)
    for i in range(n):
        if nums[i] < min_number:
            min_number = nums[i]
            answer = i
    return answer

print(solutions([7,10,5,3,2,15,19]))
print(solutions([-12, 12, 30, -15, -5, 3, 9, -11, 14]))