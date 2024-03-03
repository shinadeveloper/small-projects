##Hangman Game In python
import random
# Function to print hangman
def hangman():
  list=["apple", "banana", "orange", "grapes", "watermelon", "pineapple", "mango", "kiwi"]
  word=random.choice(list)
  print("Hello your name please")
  name=input()
  print("Hello",name,"Welcome to Hangman Game")
  print("Guess the word")
  number=len(word)
  i=0
  print('_'*number)
  guessed=[]
  count=0
  while i < (number+4) and count<=number:
    count=0
    print("enter the alphabet")
    alph=input()
    if (alph in word) :
      print("yay some more")
      guessed.append(alph)
    for i in range(number):
      if word[i] in guessed:
        print(word[i],end="")
        count+=1
      else:
        print("_",end="")
    if count==number:
      print()
      print("SUCCESS YOU WON THE GAME")
      return
    print()
  print("sorry you lost :(")
  return
hangman()