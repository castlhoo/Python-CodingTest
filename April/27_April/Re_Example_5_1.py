# 사탕 종류
# 현수는 사탕을 좋아합니다. 현수에게 사탕이 n개 있습니다.
# 현수 엄마는 현수가 요즘 너무 사탕을 많이 먹어 건강에 좋지 않다고 생각해 
# 현수에게 가지고 있는 사탕의 절반(n/2)개만 먹으라고 했습니다. 
# n은 항상 짝수입니다.
# 매개변수 nums에 현수가 가지고 있는 n개의 사탕의 종류 정보가 주어지면 
# 현수가 n/2개의 사탕을 먹는다면 
# 최대 몇 종류의 사탕을 먹을 수 있는지를 반환하는 프로그램을 작성하세요.

# 제한사항:
# • nums의 길이는 100,000을 넘지 않습니다.
# • nums[i]는 i번재 사탕의 종류를 의미합니다. nums[i]값이 같으면 같은 종류의 사탕입니다.
# • 1 <= nums[i] <= 1,000

# nums = sorted([12, 23, 11, 3, 5, 23, 23, 23, 23, 23, 23, 23])
# cnt = []
# cnt.append(nums[0])
# n = len(nums)//2

# for i in range(n):
#     if nums[i] != nums[i+1]:
#         cnt.append(i)
#     else:
#         continue


# print(sorted(nums))
# print(cnt)

def solutions(nums):
    cnt = 1
    nums .sort()
    n = len(nums)

    for i in range(1,n):
        if nums[i] != nums[i-1]:
            cnt += 1

    return cnt if cnt < n//2 else n//2

print(solutions([2, 1, 1, 3, 2, 3, 1, 2]))
print(solutions([1, 3, 5, 7, 2, 3, 7, 5, 3, 2, 5, 7, 9, 12]))
print(solutions([5, 5, 5, 5, 5, 5]))
print(solutions([12, 23, 11, 3, 5, 23, 23, 23, 23, 23, 23, 23]))
print(solutions([100, 200, 300, 400, 500, 600, 700, 800]))