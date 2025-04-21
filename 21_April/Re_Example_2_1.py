# 빈도수(ver 1)
# Direct Address Table
# 매개변수 nums에 길이가 n인 수열이 주어지면 수열의 원소중에서 
# 빈도수가 1인 가장 큰 숫자를 반환하는 프로그램을 작성하세요. 
# 빈도수 1인 숫자가 없을 경우 -1를 반환하세요.

# 제한사항:
# • nums의 길이 3 <= n <= 10,000
# • 배열 nums의 원소는 자연수입니다. 1 <= nums[i] <= 1,000

def solutions(nums):
    answer = -1
    cnt = [0]*1001

    for i in nums:
        cnt[i] += 1 # i를 만나면 i의 인덱스가 1씩 증가
    
    for j in range(1000,0,-1):
        if cnt[j] == 1:
            return j
    return answer

print(solutions([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
print(solutions([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6 ,7, 8, 8]))
print(solutions([23, 56, 11, 67, 120, 560, 812, 960, 560, 777, 888, 960]))
print(solutions([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
print(solutions([1, 3, 1, 5, 7, 2, 3, 1, 5]))