# 두 수의 차 - nlogn (정확도)
# 정확도 : 정렬된 문자에서의 특징을 찾고 비교

# 매개변수에 수열이 주어지면 수열의 nums 원소 중 
# 두 수의 차가 가장 작은 쌍을 찾아 반환하는 프로그램을 작성하세요.
# 수열의 원소는 유일값들로 이루어져 있습니다. 
# 두 수의 차가 가장 작은 쌍이 여러개면 모든
# 쌍을 배열에 담아 반환합니다. 배열에 담는 순서는 상관없습니다. 
# 단 두 수는 오름차순 정렬된쌍으로 표현합니다. 
# 정확성, 효율성테스트를 합니다.

# 제한사항:
# • nums의 길이는 100,000을 넘지 않습니다.
# • 1 <= nums[i] <= 1,000

def solutions(nums):
    answer = []
    n = len(nums)
    nums.sort()
    minN = 10000

    # O(nlogn)
    for i in range(1,n):
            diff = abs(nums[i] - nums[i-1])
            minN = min(minN, diff)

    # O(n)
    for i in range(1,n):
            diff = abs(nums[i] - nums[i-1])
            if diff == minN:
                answer.append(sorted([nums[i], nums[i-1]]))
    
    return answer

print(solutions([3, 8, 1, 5, 12]))
print(solutions([2, 1, 3, 5, 4]))
print(solutions([5, 10, 15, 20, 25, 11]))
print(solutions([2, 4, 3, 1, 5, 7, 8, 12, 13, 15, 23]))
print(solutions([100, 200, 300, 400, 120, 130, 135, 132, 121]))
