a = list(map(int, input().split()))
if len(a) == 1:
  print(True)
else:
  cs = a[1] - a[0]
  for i in range(1, len(a)):
    if a[i] - a[i - 1] != cs:
      print(False)
      quit()
  print(True)
