'''
Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed.
This function returns a string that is comprised of letters and underscores, based on what letters in lettersGuessed are in secretWord.
This shouldn't be too different from isWordGuessed!
'''

def getGuessedWord(secretWord, lettersGuessed):
    kq = ''
    for c in secretWord:
        if c not in lettersGuessed:
            kq += '_'
        else:
            kq += c
    return kq
