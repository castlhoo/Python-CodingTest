# 트럭 찾기
# 현수는 이사를 하려고 합니다.
# 이삿짐 센터에는 여러 개의 트럭이 있습니다. 
# 각 트럭은 짐을 실을 수 있는 총 무게 제한이 있습니다.
# 이사 비용은 현수가 선택한 트럭의 무게 제한에 곱하기 10을 한 값입니다.
# nums에 각 트럭의 무게 제한이 오름차순으로 주어지고, 
# 현수의 이사하는 짐의 총 무게가bweight주어지면 
# 현수가 짐을 실을 수 있는 최소비용의 트럭을 찾아 
# 선택된 트럭의 인덱스 번호를 반환하는 프로그램을 작성하세요.
# 인덱스 번호는 0번부터 시작합니다.
# 현수가 이사할 수 있는 트럭이 존재하지 않을 경우 -1를 반환합니다.

# 제한사항:
# • nums의 길이는 100,000,000을 넘지 않습니다. nums의 원소는 유일값입니다.
# • 1 <= nums[i] <= 100,000,000

# 최소무게 = 작거나 같은 값 중 큰 값(low bound search)
def solutions(nums, weight):
    n = len(nums)
    left = 0
    right = n

    while left < right:
        mid = (left + right)//2
        if weight > nums[mid]:
            left = mid + 1
        else:
            right = mid
    return -1 if right == len(nums) else right

print(solutions([100, 120, 150, 160, 165, 170, 175, 180, 190, 200], 170))
print(solutions([200, 250, 260, 265, 275, 290, 300, 325, 350, 370], 270))
print(solutions([50, 55, 60, 65, 70, 80, 90], 80))
print(solutions([20, 30, 40, 50, 60, 70], 90))
print(solutions([10, 30, 50, 70, 80, 90, 100, 110, 120], 115))