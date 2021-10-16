s1 = input()
s2 = input()
alp = 'abcdefghijklmnopqrstuvwxyz'
cnt1 = [0] * 305
cnt2 = [0] * 305
for c in s1:
    cnt1[ord(c)] += 1
for c in s2:
    cnt2[ord(c)] += 1
for c in alp:
    if min(cnt1[ord(c)], cnt2[ord(c)]) > 0:
        print('YES')
        break
else:
    print('NO')
