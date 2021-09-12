a = list(map(int, input().split()))
b = [0] * len(a)
b[0] = a[0]
for i in range(1, len(a)):
  b[i] = b[i - 1] + a[i]
for val in b:
  print(val, end = " ")
