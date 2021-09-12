'''
Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed.
This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in lettersGuessed.
'''

def getAvailableLetters(lettersGuessed):
    kq = ''
    for i in range(ord('a'), ord('z') + 1):
        c = chr(i)
        if c not in lettersGuessed:
            kq += c
    return kq
