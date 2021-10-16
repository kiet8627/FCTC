# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s.

s = input()
kq = 0
for i in range(0, len(s) - 3):
    if s[i : i + 3] == 'bob':
        kq += 1
print(kq)
