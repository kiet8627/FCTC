# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

s = input()
kq = 0
for c in s:
    if c in 'aeiou':
        kq += 1
print(kq)
