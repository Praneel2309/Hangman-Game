# Hangman game

import random

WORDLIST_FILENAME ="words.txt"



def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessedWord = guessedWord + letter
        
        else:
            guessedWord = guessedWord + '_'
    
    return guessedWord


import string 
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    allLetters = string.ascii_lowercase
    availableLetters = ''
    for letter in allLetters:
        if letter not in lettersGuessed:
            availableLetters = availableLetters + ' ' + letter
    
    return availableLetters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secretWord),"letters long.")
    print("-------------")

    guessesLeft = 8
    lettersGuessed = []

    while guessesLeft > 0 and not isWordGuessed(secretWord, lettersGuessed):
        print(f"You have {guessesLeft} guesses left.")
        print(f"Available letters: {getAvailableLetters(lettersGuessed)}")
        guess = input("Please guess a letter: ").lower()

        if guess in lettersGuessed:
            print(f"Oops! You've already guessed that letter: {getGuessedWord(secretWord, lettersGuessed)}")
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print(f"Good guess: {getGuessedWord(secretWord, lettersGuessed)}")
        else:
            lettersGuessed.append(guess)
            guessesLeft -= 1
            print(f"Oops! That letter is not in my word: {getGuessedWord(secretWord, lettersGuessed)}")
        print("------------")

    if isWordGuessed(secretWord,lettersGuessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was",secretWord)


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
