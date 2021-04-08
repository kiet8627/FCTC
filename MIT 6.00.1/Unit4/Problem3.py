def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.
 
    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    output = hand.copy()
    word_check = False
    if word in wordList:
        word_check = True
 
    letter_check = set(list(word)) <= set(output.keys())
 
    for letter in word:
        if letter in output.keys():
            output[letter] -= 1
 
    value_check = all(i >= 0 for i in output.values())
    
    if word_check == True and letter_check == True and value_check == True:
        return True
    else:
        return False
