# $Id: hangman.py ,v 1.00 2010/08/23 12:01:54 Abhainv Exp $
#@file hangman.py - a simple game of guessing letters of a word 
#@Author Abhinav S. Dangol (YIPL)


import random

def generate_word():
    word_dict = { 'orange': 'Name of a fruit' , 
                  'leg': 'a body part', 
                  'basketball': 'name of a sports', 
                  'laptop' : 'type of technology' , 
                  'nepal':'name of a country',
                  'abhinav': 'my name',
                  'yipl': 'organization'
                }
                
    words = word_dict.keys()
    rand = random.randint(0,len(words)-1)
    selected_word = words[rand]
    hint = word_dict[selected_word]
    word_list = [selected_word, hint]
    return word_list

secret = generate_word()
#print secret[1]

count = len(secret[0])
#print count

guesses = ''
chance = 0

while chance != 6 :
    blank = 0
    print "\n" 
    for l in secret[0]:
        if l in guesses:
            print l,
        else:
            print '_',
            blank += 1
    
    print "\n\n" + secret [1]
    print

    if blank == 0:
        print 'You win!'
        break

    guess = raw_input('guess a letter: ')
    if len(guess)>1:
        print 'please enter a correctly'
        break
    
    guesses += guess
    
    if guess not in secret[0]:
        chance += 1
        #print 'Nope.'
        #print chance, 'more chance'
        if chance >= 1: print '   O   '
        if chance >= 2: print ' \_|_/ '
        if chance >= 3: print '   |   '
        if chance >= 4: print '  / \  '
        if chance >= 5: print ' d   b '
        if chance == 6:
          print 'The answer is', secret[0]