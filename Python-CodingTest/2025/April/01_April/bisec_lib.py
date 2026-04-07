from bisect import bisect_left, bisect_right
# bisec_left = lower bound
# bisec_rigth = upper bound

def solutions(nums, weight):
    answer1 = bisect_left(nums, weight)
    answer2 = bisect_right(nums, weight)
    return answer1, answer2 # 3(8), 4(10)
    return -1 if answer1 == len(nums) or answer2 == len(nums) else answer1, answer2
print(solutions([2, 5, 7, 8, 10, 15, 20, 24, 25, 30], 8))