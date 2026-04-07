# 고정된 숫자
# 오름차순으로 정렬된 일차원 배열의 원소 중 
# 인덱스 번호(인덱스 번호는 0번부터 시작합니다.)와 
# 자기 자신의 값이 같으면 이 원소를 고정된 숫자라고 합니다.
# 예를 들어 [-3, -2, 0, 1, 3, 5, 8, 9, 12] 배열에서 고정된 숫자는 5입니다. 
# 배열 원소 5의 인덱스 번호가 5로 원소와 인덱스 값이 같습니다.
# 매개변수 nums에 오름차순으로 정렬된 정수 배열이 주어지면 
# 배열 원소 중 고정된 숫자를 찾아 반환하는 프로그램을 작성하세요.
# 고정된 숫자는 유일합니다. 고정된 숫자가 없다면 -1를 반환하세요.

# 제한사항:
# • nums의 길이는 1,000,000을 넘지 않습니다. nums의 원소는 유일값입니다.
# • -100,000,000 <= nums[i] <= 100,000,000

def solutions(nums):
    n = len(nums)
    left = 0
    right = n

    while left < right:
        mid = (left + right)//2
        if mid > nums[mid]:
            left = mid + 1
        else:
            right = mid
    return -1 if right != nums[right]  else right

print(solutions([-3, -2, 0, 1, 3, 5, 8, 9, 12]))
print(solutions([-10, -5, -2, 3, 4, 6, 7, 8]))
print(solutions([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(solutions([-5, -3, 0, 1, 2, 3, 4, 7]))
print(solutions([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))