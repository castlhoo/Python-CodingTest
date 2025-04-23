# 팰린드롬 길이
# 문자열이 주어지면 해당 문자열의 문자들을 가지고 만들 수 있는 
# 최대길이 팰린드롬을 만들고 그 길이를 구하세요. 
# 문자열은 소문자로만 이루어져 있습니다.
# 만약 "abcbbbccaaeee" 가 주어진다면 
# 만들 수 있는 가장 긴 팰린드롬은 "ebbcaaacbbe"이고 답은 11입니다.

# 제한사항:
# • s의 길이는 1,000을 넘지 않습니다
from collections import Counter

def solution(s):
    nH = Counter(s)
    total = sum(nH.values())
    cnt = 0

    for x in nH:
        if nH[x] % 2 != 0:
            cnt += 1
        
    total = total - (cnt - 1)
    return total

print(solution("abcbbbccaaeee"))
print(solution("aabbccddee"))
print(solution("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"))
print(solution("aabcefagcefbcabbcc"))
print(solution("abcbbbccaa"))