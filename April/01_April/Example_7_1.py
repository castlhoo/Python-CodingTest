# 이진 탐색
# nums에 오름차순으로 정렬된 정수 배열이 주어지고, 
# target에 nums배열에서 찾고자 하는 값이 주어지면 
# nums배열에서 target의 인덱스 번호를 찾아 반환하는 프로그램을 작성하세요.
# 인덱스 번호는 0번부터 시작합니다.
# target값이 nums에 존재하지 않을 경우 -1를 반환합니다.

# 제한사항:
# • nums의 길이는 100,000,000을 넘지 않습니다. nums의 원소는 유일값입니다.
# • -100,000,000 <= nums[i] <= 100,000,000

def solutions(nums, target):
    n = len(nums)
    left = 0
    right = n-1

    while left <= right:
        mid = (left+right)//2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    # 못 찾을 시, 
    return -1

print(solutions([2, 5, 7, 8, 10, 15, 20, 24, 25, 30], 8))
print(solutions([-3, 0, 2, 5, 8, 9, 12, 15], 0))
print(solutions([-5, -2, -1, 3, 8, 9, 12, 17, 23], 2))
print(solutions([3, 6, 9, 12, 17, 29, 33], 3))
print(solutions([1, 2, 3, 4, 5, 7, 9, 11, 12, 15, 16, 17, 18], 18))