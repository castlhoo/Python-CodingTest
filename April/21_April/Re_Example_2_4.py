# 팰린드롬 확인
# 소문자로만 이루어진 문자열이 주어지면 
# 해당 문자열의 문자들의 순서를 재배치해서 
# 팰린드롬(회문)을 만들 수 있는지를 확인하고 싶습니다. 
# 만약 "abbac"같은 문자열은 문자들을 "abcba"로 
# 재 배치하면 팰린드롬을 만들 수 있습니다.
# 매개변수 s에 문자열이 주어지면 해당 문자열이 재 배치를 통해 
# 팰린드롬을 만들 수 있으면 True를 
# 못 만들면 False를 반환하는 프로그램을 작성하세요.

# 제한사항:
# • s의 길이는 1,000을 넘지 않습니다.

from collections import Counter

def solutions(s):
    cnt = 0
    nH = Counter(s)
    
    for key in nH:
        if nH[key] % 2 != 0:
            cnt += 1
    
    return cnt <= 1

def solutions2(s):
    return sum(x % 2 for x in Counter(s).values()) <= 1

print(solutions("abacbaa"))
print(solutions("abaaceeffkckbaa"))
print(solutions("abcabbcc"))
print(solutions("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
print(solutions("aabcefagcefbcabbcc"))