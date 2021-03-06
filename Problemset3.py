# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r') #change to work in python3
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()               #change to work in python3
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
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
    # FILL IN YOUR CODE HERE...
    return set(secretWord) <= set(lettersGuessed)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    w=''
    for i in secretWord:
        if i in lettersGuessed:
            w+=i
        else:
            w+=' _ '
    return w



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    q=''
    alphabet=list(string.ascii_lowercase)
    for i in alphabet:
        if i not in lettersGuessed:
            q+=i
    return q

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
    # FILL IN YOUR CODE HERE...
    guessleft=8
    guess=[]
    print("Welcome to the game, Hangman!")
    print('I am thinking of a word that is {} letters long.'.format(len(secretWord)))
    print("-------------")
    i=1
    while i<=guessleft:
        print('\nYou have {} guesses left.'.format(guessleft))
        print("\nAvailable letters: {}".format(getAvailableLetters(guess)))
        g0=input('\nPlease guess a letter:')
        g=g0.lower()
        if g in guess:
            print("\nOops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, guess)))
        
        elif g in secretWord:
            guess.append(g)
            print("\nGood guess: {}".format(getGuessedWord(secretWord, guess)))
            if isWordGuessed(secretWord, guess):
                print("\nCongratulations, you won!")
                ans=input('Do you want to start a new game?(press y for yes')  # start a new game
                if ans=='y':
                    newgame()
                else:
                    pass
                break
        else:
            guess.append(g)
            print("\nOops! That letter is not in my word: {}".format(getGuessedWord(secretWord, guess)))
            guessleft-=1
            if guessleft==0:
                print("Sorry, you ran out of guesses. The word was else.")
                print("word was: {}".format(secretWord))
                ans=input('Do you want to start a new game?(press y for yes')  # start a new game
                if ans=='y':
                    newgame()
                else:
                    pass
    

    
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)


def newgame():
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
newgame()
