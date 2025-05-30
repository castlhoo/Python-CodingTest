# 매개변수 nums에 길이가 n인 수열이 주어지면 수열의 원소중에서 빈도수가 1인 가장 큰 숫자
# 를 반환하는 프로그램을 작성하세요. 빈도수 1인 숫자가 없을 경우 -1를 반환하세요.

# # 제한사항:
# # • nums의 길이 3 <= n <= 10,000
# # • 배열 nums의 원소는 자연수입니다. 1 <= nums[i] <= 1,000
def solution(nums):
    answer = -1 # 빈도수가 1인 숫자가 없을때를 기본값으로 설정
    cnt = [0] * 1001

    for x in nums:
        cnt[x] += 1 # 각 배열에 해당하는 키값에 숫자가 증가
                    # 2는 1, 3은 1, 9는 3,,,반복하면서 숫자를 만나면 1더하기
    for i in range(1000, 0, -1): # i가 큰 값부터 돌기때문
        if cnt[i] == 1:
            return i
            
    return answer


print(solution([3,9,2,12,9,12,8,7,9,12]))
print(solution([2,1,3,2,1,3,4,5,4,5,6,7,6,7,8,8]))
