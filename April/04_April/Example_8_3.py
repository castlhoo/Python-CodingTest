# 연속된 문자 지우기
# 매개변수 s에 문자열이 주어지면 이웃한 두 개의 문자가 같으면 
# 두 문자를 제거합니다. 이 과정을 반복해서 
# 최종적으로 남는 문자만으로 이루어진 
# 문자열을 반환하는 프로그램을 작성하세요.
# 만약 "acbbcaa"라는 문자열이 주어진다면 
# 최초 bb가 연속되어 있어 제거하고 나면 "accaa"가되고, 
# 다시 cc가 연속되어 제거하면 "aaa"가 되고 "aa"연속되어 제거하면 
# "a"가 최종적으로 남습니다.

# 제한사항:
# • 문자열 s의 길이는 100,000을 넘지 않습니다.
# • 문자열 s는 소문자로만 이루어져 있습니다

def solutions(s):
    answer = []

    for i in s:
        # 스택이 비어있지 않고, 스택의 마지막 문자와 현재 문자가 같다면
        # if answer는 boolean으로 응답가능하기 때문
        if answer and answer[-1] == i:
            answer.pop()
        else:
            answer.append(i)
    
    return "".join(answer)

print(solutions("acbbcaa"))
print(solutions("bacccaba"))
print(solutions("aabaababbaa"))
print(solutions("bcaacccbaabccabbaa"))
print(solutions("cacaabbc"))