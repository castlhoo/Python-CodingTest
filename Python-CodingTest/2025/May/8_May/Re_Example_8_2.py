# Backspace
# 현수는 주어진 문자열의 문자 순서대로 키보드 자판의 문자를 쳐 
# 화면에 s문자열을 작성합니다. 
# 문자열에는 '#'문자가 있는데 이 문자는 Backspace키를 의미합니다.
# 매개변수 s에 현수가 키보드 자판을 쳐야할 순서인 문자열이 주어지면 
# 현수가 s문자열을 작성했을 때 최종적으로 화면에 작성된 문자열을 
# 반환하는 프로그램을 작성하세요.
# 화면에는 적어도 문자 한 개는 작성되어 있습니다.

def solutions(s):
    answer = []

    for i in s:
        if i == "#":
            answer.pop()
        else:
            answer.append(i)

    return "".join(answer)

print(solutions("abc##ec#ab"))
    