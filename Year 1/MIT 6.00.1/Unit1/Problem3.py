# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.

s = input()
kq = ''
_s = s[0]
for i in range(1, len(s)):
    if s[i] >=  s[i - 1]:
        _s += s[i]
    else:
        if len(_s) > len(kq):
            kq = _s
            _s = s[i]
if len(_s) > len(kq):
    kq = _s
print(kq)
