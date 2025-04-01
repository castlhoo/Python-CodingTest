# 카드 점수 (Ok^2)
# N개의 카드가 일렬로 놓여져 있습니다. 각 카드에는 숫자가 적혀있습니다.
# 현수는 카드가 일렬로 놓여진 줄의 양 끝 
# 즉 왼쪽 맨 끝카드와 오른쪽 맨 끝 카드 둘 중 하나를 가져갈 수 있습니다. 
# 현수는 양 끝에서 가져가는 방식으로 k개의 카드를 가져갈 수 있습니
# 다. 그리고 가져간 카드에 적혀진 숫자의 총합이 현수가 얻는 점수입니다.
# 일려로 놓여진 각 카드의 숫자가 매개변수 nums에 주어지고, 
# 현수가 가져갈 수 있는 카드의 개수 k가 주어지면 
# 현수가 얻을 수 있는 최대점수를 반환하는 프로그램을 작성하세요.

# 제한사항:
# • nums의 길이는 300,000을 넘지 않습니다.
# • nums의 원소는 100을 넘지 않는 자연수입니다..
# • 2 <= k < nums의 길이
def solutions(nums, k):
    answer = 0
    n = len(nums)

    for i in range(k+1): # 총 경우의 수
        sumN = 0
        for j in range(i): # 왼쪽
            sumN += nums[j]
        for j in range(n-k+i, n): # 오른쪽
            sumN += nums[j]
        answer = max(answer, sumN)
    return answer

print(solutions([2, 3, 7, 1, 2, 1, 5], 4))
print(solutions([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
print(solutions([1, 30, 3, 5, 6, 7], 3))
print(solutions([1, 2, 15, 3, 6, 7, 8, 9], 5))
print(solutions([12, 5, 6, 12, 34, 35, 13, 3, 7, 8, 9] ,7))