a = list(map(int, input().split()))
n = len(a)
if n <= 2:
    print(n)
    quit
kq = 0
cur = 0
for i in range(0, n - 2):
    for j in range(i + 1, n - 1):
        arr = []
        diff = a[j] - a[i]
        if diff == 0:
            continue
        arr.append(a[i])
        arr.append(a[j])
        for k in range(j, n):
            if a[k] - arr[len(arr) - 1] != diff:
                continue
            arr.append(a[k])
            cur = len(arr)
            kq = max(kq, cur)
print(kq)
