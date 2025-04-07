# 샌드위치
# 현수는 샌드위치를 만들려고 합니다.
# 식탁에 샌드위치 재료인 식빵과 토마토가 일렬로 놓여 있습니다.
# 현수가 만드는 샌드위치는 식빵-토마토-식빵 순으로 합쳐서 포장을 합니다. 
# 현수는 식탁에 놓여 있는 재료의 순서를 유지하면서 샌드위치를 만들어야 합니다.
# 만약 식탁에 
# [식빵, 식빵, 식빵, 토마토, 식빵, 식빵, 토마토, 식빵, 토마토, 식빵] 순으로 
# 놓여있다면 현수는 3번째, 4번째, 5번째를 합쳐서 샌드위치를 만들고, 
# 6번째, 7번째, 8번째를 합쳐서 샌드위치를 만들고, 
# 2번째, 9번째, 10번째를 합쳐서 샌드위치를 만들어 
# 총 3개의 샌드위치를 만들 수 있습니다. 
# 매개변수 nums에 식탁에 놓여 있는 샌드위치 재료의 정보가 주어지면 
# 현수가 만들 수 있는 샌드위치의 총 개수를 반환하는 프로그래을 작성하세요.

# 제한사항:
# • nums의 길이는 1,000을 넘지 않습니다.
# • nums[i]값은 1 또는 2입니다. 1은 식빵을 의미하고, 2는 토마토를 의미합니다.
def solutions(nums):
    answer = 0
    stack = []

    for i in nums:
        if len(stack) > 2 and i == 1 and stack[-1] == 2 and stack[-2] == 1:
            answer+=1
            stack.pop()
            stack.pop()
        else:
            stack.append(i)
    return answer

print(solutions([1,1,1,2,1,1,2,1,2,1]))
print(solutions([2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1]))
print(solutions([1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1]))
print(solutions([2, 1, 1, 1, 2, 1, 2]))
print(solutions([1, 1, 1, 1, 1, 1, 1]))