# 팰린드롬 길이
# 문자열이 주어지면 해당 문자열의 문자들을 가지고 만들 수 있는 최대길이 팰린드롬을 만들고
# 그 길이를 구하세요. 문자열은 소문자로만 이루어져 있습니다.
# 만약 "abcbbbccaaeee" 가 주어진다면 만들 수 있는 가장 긴 팰린드롬은 "ebbcaaacbbe"이고
# 답은 11입니다.

# 제한사항:
# • s의 길이는 1,000을 넘지 않습니다
from collections import Counter  # 문자열 내 문자 개수를 쉽게 세기 위해 Counter 사용

def solution(s):
    Pd = Counter(s)  # 문자열 s의 각 문자의 등장 횟수를 저장하는 딕셔너리
    count_pd = list(Pd.values())  # 등장 횟수 값들만 리스트로 저장

    odd_count = 0  # 홀수 개수 카운트
    for j in count_pd:
        if j % 2 != 0:  # 만약 등장 횟수가 홀수라면
            odd_count += 1  # 홀수 개수 증가
    
    # s의 길이에서 홀수 갯수를 빼고 하나를 더해주기 *특징파악 중요
    return len(s) - odd_count + 1 if odd_count > 0 else len(s)

# 테스트 케이스 실행
print(solution("abcbbbccaaeee"))  # True
print(solution("aabbccddee"))  # True
print(solution("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"))  # False
print(solution("aabcefagcefbcabbcc"))  # True
print(solution("abcbbbccaa"))  # False
