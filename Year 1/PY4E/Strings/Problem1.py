a = input()
b = input()
c = input()
if '?' in a:
    num = int(c) - int(b)
    num = str(num)
    print(num[a.find('?')])
elif '?' in b:
    num = int(c) - int(a)
    num = str(num)
    print(num[b.find('?')])
else:
    num = int(a) + int(b)
    num = str(num)
    print(num[c.find('?')])
