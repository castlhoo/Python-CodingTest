from collections import Counter

n, m = map(int, input().split())


count = Counter()
result = []
for i in range(1, n+1):
    for j in range(1, m+1):
        count[i+j] += 1

max_count = max(count.values())
result = [key for key, value in count.items() if value == max_count]
result.sort()
print(result)
            