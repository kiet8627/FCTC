a = list(map(int, input().split()))
if len(a) == 1:
  print(True)
else:
  if a[0] < a[1]:
    for i in range(1, len(a) - 1):
      if a[i] >= a[i + 1]:
        print(False)
        quit()
    print(True)

  elif a[0] > a[1]:
    for i in range(1, len(a) - 1):
      if a[i] <= a[i + 1]:
        print(False)
        quit()
    print(True)

  else:
    print(False)
