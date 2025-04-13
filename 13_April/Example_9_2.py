# 피보나치 수열
# 피보나치 수열의 n번째 항은 n-1번째 항과 n-2번째 항을 합으로 구합니다.
# 피보나치 수열의 첫 번째 항과 두 번째 항은 1입니다.
# 피보나치 수열을 구해보면
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ......
# 입니다.
# 매개변수 n에 구해야 할 피보나치 수열의 항 번호가 주어지면 피보나치 수열의 n번째 항을 구
# 해 반환하는 프로그램을 작성하세요.

# 제한사항:
# • 1 <= n <= 12

def solutions(n):
    if n == 1 or n == 2:
        return 1
    else:
        return solutions(n-2) + solutions(n-1)
    
print(solutions(5))
print(solutions(6))
print(solutions(8))
print(solutions(10))