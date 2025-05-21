n = int(input())
a = list(map(int, input().split()))

avg = round(sum(a)/n)
min_diff = float('inf')
max_score = -1
result_idx = 0

for idx, score in enumerate(a, start=1):
    diff = abs(score-avg)

    if diff < min_diff:
        min_diff = diff
        max_score = score
        result_idx = idx
        
    elif diff == min_diff:
        if score > max_score:
            max_score = score
            result_idx = idx
            
        elif score == max_score:
            if result_idx > idx:
                result_idx = idx

print(avg, result_idx)