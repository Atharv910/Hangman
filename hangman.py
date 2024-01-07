import os

word = input("Type in a word for the other person to guess! ")
os.system("cls")
guess_list = []

for i in range(len(word)):
    if ' ' in word[i]:
        print('     ', end = "")
    else:
        print("_   ", end = "")
   
    
hangman = ['''
  +---+
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


mistakes_done = 0 
guessed_yet = False
letters_guessed = 0
length = len(word)

if ' ' in word:
    length = len(word) - 1
    
    
while letters_guessed < length and mistakes_done < 7:
    guess = input("\nGuess a letter: ")
    while guess in guess_list:
        print("You've already guessed this letter! Choose another letter please.")
        guess = input("Guess a letter: ")
    guess_list.append(guess)
    if guess in word:
        letters_guessed += word.count(guess)
        guessed_yet = True
        for i in word:
            if i in guess_list:
                print(i,' ', end = ""),
            elif i == ' ':
                print('     ', end = "")
            else:
                print("_   ", end = ""),
        print(hangman[mistakes_done])
    else:
        mistakes_done += 1
        print (hangman[mistakes_done])
        print("Oops, that's wrong! Try again!")
        if guessed_yet:
            for i in word:
                if i in guess_list:
                    print(i,' ', end = ""),
                elif i == ' ':
                    print('     ', end = "")
                else:
                    print("_   ", end = ""),
        else:
            for i in range(len(word)):
                if ' ' in word[i]:
                    print('    ', end = "")
                else:
                    print("_   ", end = "")              

if mistakes_done < 7:
    print("\nCongrats! You guessed the word!")
else:
    print("\nOh no! You ran out of tries!")