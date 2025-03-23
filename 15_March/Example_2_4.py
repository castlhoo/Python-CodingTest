# 팰린드롬 확인
# 소문자로만 이루어진 문자열이 주어지면 해당 문자열의 문자들의 순서를 재배치해서 팰린드롬
# (회문)을 만들 수 있는지를 확인하고 싶습니다. 만약 "abbac"같은 문자열은 문자들을 "abcba"
# 로 재 배치하면 팰린드롬을 만들 수 있습니다.
# 매개변수 s에 문자열이 주어지면 해당 문자열이 재 배치를 통해 팰린드롬을 만들 수 있으면
# True를 못 만들면 False를 반환하는 프로그램을 작성하세요.

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

    return odd_count <= 1  # 홀수 개수가 1개 이하이면 팰린드롬 가능 (True), 그렇지 않으면 False

# 테스트 케이스 실행
print(solution("abacbaa"))  # True
print(solution("abaaceeffkckbaa"))  # True
print(solution("abcabbcc"))  # False
print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))  # True
print(solution("aabcefagcefbcabbcc"))  # False
