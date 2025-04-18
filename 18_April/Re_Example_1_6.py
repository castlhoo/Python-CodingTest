# RE
# 두 수의 합
# 정수 수열 안에서 수열의 원소 두 개의 합이 target값이 되는 경우를 찾고 싶습니다.
# 매개변수 nums에 길이가 n인 수열이 주어지고, 
# 매개변수 target에 자연수 값이 주어지면 이 수열안에서 두 개의 원소의 합이 
# 정수 target값이 되는 두 원소를 구해 배열에 오름차순으로 담아 반환합니다.
# 두 개의 원소의 합이 target값이 되는 경우는 오직 한가지 뿐인 입력만 주어집니다. 
# 한 원소를 두 번 더하는 것은 안됩니다. 
# nums의 각 원소는 유일값입니다.
# 답이 없을 경우 [0, 0]을 반환합니다.

# 제한사항:
# • nums의 길이 3 <= n <= 10,000
# • 배열 nums의 원소는 정수입니다. -10,000 <= nums[i] <= 10,000
# • -20,000 <= target <= 20,000

def solutions(nums, target):
    n = len(nums)

    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return sorted([nums[i], nums[j]])
    return [0,0]

print(solutions([7, 3, 2, 13, 9, 15, 8, 11], 12))
print(solutions([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
print(solutions([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
print(solutions([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
print(solutions([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
print(solutions([7, 5, 12, 20], 15))