# 소수(에라토스테네스 체)
# 자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
# 만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
# 제한시간은 1초입니다.
# ▣ 입력설명
# 첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.
# ▣ 출력설명
# 첫 줄에 소수의 개수를 출력합니다.
# ▣ 입력예제 1
# 20
# ▣ 출력예제 1
# 8

# Solution 1
import math

n = int(input())
result = []

for i in range(2, n+1):
    is_prime = True
    for j in range(2, int(math.sqrt(i))+1):
        if i % j ==0:
            is_prime = False
            break
    
    if is_prime:
        result.append(i)


print(len(result))

# Solution 2
n = int(input())
cnt = 0
ch = [0]*(n+1)

for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1

print(cnt)