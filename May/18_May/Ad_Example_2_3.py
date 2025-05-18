n,k = map(int, input().split())
a = list(int, input().split())
res = set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
res = list(res)
print(res[k-1])