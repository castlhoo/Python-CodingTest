# 올바른 괄호
# 괄호 문자열이 입력되면 올바른 괄호이면 "YES", 올바르지 않으면 "NO"를 출력합니다.
# (())() 이것은 괄호의 쌍이 올바르게 위치하는 거지만, (()()))은 올바른 괄호가 아니다.
def solutions(s):
    answer = "YES"
    stack = []

    for i in s:
        if i == ")":
            if len(stack) == 0:
                return "NO"
            else:
                stack.pop()
        else:
            stack.append(i)

    if len(stack) > 0:
        return 'NO'
    
    return answer

print(solutions("((()))()"))
print(solutions("(()(()"))