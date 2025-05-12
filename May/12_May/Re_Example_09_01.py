# n! 구하기
# 매개변수 n에 자연수가 입력되면 n!(n팩토리얼) 값을 구하여 반환하는 
# 프로그램을 작성하세요.
# 예를 들어 n = 5라면 5! = 5 * 4 * 3 * 2* 1 = 120을 반환하면 됩니다.

def solutions(n):
    
    if n == 1:
        return 1
    else:
        return n * solutions(n-1)

print(solutions(5))