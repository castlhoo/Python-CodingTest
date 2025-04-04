# 올바른 괄호 (괄호, 음수-양수와 같은 쌍찾기 문제는 거의 스택)
# 괄호 문자열이 입력되면 올바른 괄호이면 "YES", 
# 올바르지 않으면 "NO"를 출력합니다.
# (())() 이것은 괄호의 쌍이 올바르게 위치하는 거지만, 
# (()()))은 올바른 괄호가 아니다.

# 제한사항:
# • 문자열 s의 길이는 100을 넘지 않습니다.

def solutions(s):
    answer = "YES"
    stack = []
    for i in s:
        if i == ")":
            if len(stack) == 0:
                return "No"
            stack.pop() # 꺼내서 쌍 찾기
        else:
            stack.append(i)
    
    if len(stack) > 0:
        return "No"

    return answer

print(solutions("((()))()"))
print(solutions("(()(()"))
print(solutions("()())"))
print(solutions("())("))
print(solutions("((())))()("))