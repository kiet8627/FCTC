s = input()
kq = 1
cnt = [0] * 123
i = 0
while i < len(s):
    cnt[ord(s[i])] += 1
    if cnt[ord(s[i])] > 1:
        j = 1
        while j < len(s):
            cnt[ord(s[j])] = 0
            j += 1
        i -= 1
        kq += 1
    i += 1
print(kq)
