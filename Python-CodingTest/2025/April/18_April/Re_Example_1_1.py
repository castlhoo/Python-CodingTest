# RE
# 최솟값의 위치
# 수열의 원소에서 가장 작은 값을 찾고 싶습니다.
# 매개변수 nums에 길이가 n인 수열이 주어지면 
# 수열의 원소중에서 가장 작은 값을 찾아 
# 그 값의 nums 배열의 인덱스 번호를 반환하는 프로그램을 작성하세요.
# 배열의 인덱스 번호는 0부터 시작합니다.

# 제한사항:
# • nums의 길이 3 <= n <= 100,000
# • 배열 nums의 원소는 정수입니다. -1,000,000 <= nums[i] <= 1,000,000
# • 배열 nums의 원소는 중복된 값이 존재하지 않습니다.
def solutions(nums):
    answer = 0
    min_number = 10000000
    n = len(nums)

    for i in range(n):
        if nums[i] < min_number:
            min_number = nums[i]
            answer = i
    return answer    

print(solutions([7, 10, 5, 3, 2, 15, 19]))
print(solutions([-12, 12, 30, -15, -5, 3, 9, -11, 14]))
print(solutions([17, 11, 5, 8, 23, 29, 19, 12, 25, 16, 2]))
print(solutions([7, 5, 12, -9, -12, 22, -30, -35, -21]))