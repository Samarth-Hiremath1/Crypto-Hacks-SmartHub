import random
import math
import time
from os import system
def clear():
  _=system("clear")

#Sambhav's Calculator Program
def calculator():  
  def addition(firstaddition1,secondaddition2):
      print("The answer is: "+ str(firstaddition1+secondaddition2))
      
  def subtraction(firstsubtraction1,secondsubtraction2):
      print("The answer is: "+ str(firstsubtraction1 - secondsubtraction2))

  def multiplication(firstmultiplication1, secondmultiplication2):
    print("The answer is:" + str(firstmultiplication1 * secondmultiplication2))

  def division(firstdivision1, seconddivision2):
    print("The answer is:" + str(firstdivision1 * seconddivision2))

  

  #main
  print("Calculator!")
  what = input("What would you like to calculate: \nAddition?\nSubtraction?\nMultiplication? \nDivision? \nQuadratics? \n\n\n\n")

  what = what.lower()
  if (what == "addition"):
      firstaddition = int(input("enter your first number: "))
      secondaddition = int(input("enter your second number: "))
      addition(firstaddition,secondaddition)

  if (what == "subtraction"):
      firstsubtraction = int(input("enter your first number: "))
      secondsubtraction = int(input("enter your second number: "))
      subtraction(firstsubtraction,secondsubtraction)

  if (what == "multiplication"):
      firstmultiplication = int(input("enter your first number: "))
      secondmultiplication = int(input("enter your second number: "))
      multiplication(firstmultiplication,secondmultiplication)

  if (what == "division"):
      firstdivision = int(input("enter your first number: "))
      seconddivision = int(input("enter your second number: "))
      division(firstdivision,seconddivision)

  if (what == "quadratics"):
      print("To use this function: type in everything with a space besides the sign with the number and the variable...")
      quadratics = input("enter the equation:\n")
      ar = quadratics.split(" ")
      a = ar[0]
      
      b = ar[2]
    
      c = ar[4]
        
      a = float(a)
      b = float(b)
      c = float(c)
      
      
      
      discriminant = (b**2) - (4*a*c)
    
      if (discriminant < 0):
          print("imaginary: " + str(discriminant))
      if (discriminant>=0):
          value = math.sqrt(discriminant)
        
          b = (b*-1)
        
          #first numbers
          top = b+value
        
          bottom= 2*a
          equal=top/bottom
          
          if (equal >= 0):
            print("First Factor: (x - " + str(equal) + ")")
          else:
            equal = equal *-1
            print("First Factor: (x " + str(equal) + ")")
            equal = equal *-1
          
          #second number
          up = b-value
          
          negative=up/bottom
          
          if (negative >= 0):
            print("Second Factor: (x - " + str(negative) + ")" )
          else:
            negative = negative *-1
            print("Second Factor : (x + " + str(negative) + ")")
            negative = negative *-1
          print("x = " + str(equal))
          print("x = " + str(negative))
          print("\n\n\n\n")

######################END OF CALCULATOR#####################


#Samarth's Hangman Program
def hangman():

  def main():
      welcome = ['Welcome to Hangman! A word will be chosen at random and',
                'you must try to guess the word correctly letter by letter',
                'before you run out of attempts. Good luck!'
                ]

      for line in welcome:
          print(line, sep='\n')


      play_again = True

      while play_again:
          words = ["hangman",
                  "chairs", "backpack", "bodywash", "clothing",
                  "computer", "python", "program", "glasses", "sweatshirt",
                  "sweatpants", "mattress", "friends", "clocks", "biology",
                  "algebra", "suitcase", "knives", "ninjas", "shampoo"]

          chosen_word = random.choice(words).lower()
          player_guess = None # will hold the players guess
          guessed_letters = [] # a list of letters guessed so far
          word_guessed = []
          for letter in chosen_word:
              word_guessed.append("-") 
          joined_word = None 

          HANGMAN = (
  """
  -----
  |   |
  |
  |
  |
  |
  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  |
  |
  |
  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  |  -+-
  |
  |
  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-
  |
  |
  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-\ 
  |
  |
  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-\ 
  |   | 
  |
  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-\ 
  |   | 
  |   | 
  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-\ 
  |   | 
  |   | 
  |  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-\ 
  |   | 
  |   | 
  |  | 
  |  | 
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-\ 
  |   | 
  |   | 
  |  | | 
  |  | 
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-\ 
  |   | 
  |   | 
  |  | | 
  |  | | 
  |
  --------
  """)

          print(HANGMAN[0])
          attempts = len(HANGMAN) - 1


          while (attempts != 0 and "-" in word_guessed):
              print(("\nYou have {} attempts remaining").format(attempts))
              joined_word = "".join(word_guessed)
              print(joined_word)

              try:
                  player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
              except:
                  print("That is not valid input. Please try again.")
                  continue                
              else: 
                  if not player_guess.isalpha(): 
                      print("That is not a letter. Please try again.")
                      time.sleep(1.5)
                      continue
                  elif len(player_guess) > 1: 
                      print("That is more than one letter. Please try again.")
                      time.sleep(1.5)
                      continue
                  elif player_guess in guessed_letters: 
                      print("You have already guessed that letter. Please try again.")
                      time.sleep(1.5)
                      continue
                  else:
                      pass

              guessed_letters.append(player_guess)

              for letter in range(len(chosen_word)):
                  if player_guess == chosen_word[letter]:
                      word_guessed[letter] = player_guess

              if player_guess not in chosen_word:
                  attempts -= 1
                  print(HANGMAN[(len(HANGMAN) - 1) - attempts])

          if "-" not in word_guessed: 
              print(("\nCongratulations! {} was the word").format(chosen_word))
          else: 
              print(("\nUnlucky! The word was {}.").format(chosen_word))

          print("\nWould you like to play again?")

          response = input("> ").lower()
          if response not in ("yes", "y"):
              play_again = False
          else:
            print("Thanks for playing Hangman!")
            time.sleep(2)
            clear()

  if __name__ == "__main__":
      main()

#######################END OF HANGMAN######################


#Samarth's Fun Jokes
def fun_jokes():
  print("Hey there! \nAre you feeling bored?\nAre you in need of some jokes? \nIf yes, then this is perfect for you!")
  print("\n")

  jokes = ["My boss told me to nail 2 pieces of wood", "How did Darth Vader know what Luke Skywalker would get for Christmas?","When I found out that my toaster wasn't water proof","What's red and smells like blue paint?","Why do seagulls live by the sea?","Why couldn't the pirates play cards?","How did the barber win the race?","What do you get when you cross a snake and a frog?","What is brown and sticky?","What did the pony say when he had a sore throat?","What did the fish say when it ran into a wall?","How to make a Kleenex dance?","I am thinking of going to Switzerland for a vacation.","Why can't a bicycle stand on its own?","What type of shoes do rich people wear?","What font does a witch write in?"]

  ans = ["I nailed it.", "He felt his presence.","I was shocked!","Red paint.","Because if they live by the bay, they would be Bagels.","Because the Captian was standing on the deck.","Because he knew a short cut.","A jump rope!","A stick!","He was just a little hoarse.","Dam","You put a little boggie in it!","I mean the flag is a big plus!","Because its two-tired!","Cashews!","Cursive!"]

  r = -1
  j=0
  a=0
  while r != 0:
    
    while r!=0:
      r=int(input("Enter a number for a joke. Enter 0 to end the program."))
      if(r == 0):
        print("Thanks for playing Fun Jokes!")
        time.sleep(2)
        clear()
        break
      rand_idx = random.randint(0, len(jokes)-1)
      a=j
      print(jokes[rand_idx])
      time.sleep(2)
      print(ans[rand_idx])
      time.sleep(2.5)
      clear()

#####################END OF FUN JOKES#####################      

##############community service
def bettercommunity():
  journal = []
  start = input("What would you like to know about? Littering, Speed driving, the Homeless, or Blood shortage?")
  if (start == "Littering" or start == "littering"):
      print("The amounts of liter in you community could be small. But the impact os great." + "\n" +"Random wastes thrown can clog strom water drain. This causes floods in the" + "\n" + "community, and the water does not always drain quickly.")
      record = input("A small action can make a big change. Start it off! What would you like to do?")
      journal.append(record)
      
  if (start == "Speed driving" or start == "speed driving" or start == "Speed Driving"):
      print("A community is small, but there are speed limits. They need" + "\n" + "to be strictly followed because it is not only you, but other cars, " + "\n" + "and people will be on the road." + "\n" + "Accidents can happen anytime, anywhere." + "\n" + "Every victim has family waiting for them.")
      record = input("A small action can make a big change. Start it off! What would you like to do?")
      journal.append(record)
      
  if (start == "the Homeless" or start == "The Homeless" or start == "the homeless"):
      print("Homes are lost everyday. Without a shelter, security, and proper resources, hundreds of thousands,553,742 people in the US, to be presice, are roaming on the streets.")
      record = input("A small action can make a big change. Start it off! What would you like to do?")
      journal.append(record)
            
  if (start == "Blood Shortage" or start == "blood shortage" or start == "Blood shortage"):
      print("A parent's hard skips a beat, when they heard that their child" + "\n" + "is short of blood. It is not guaranteed that the correct blood group will be found" + "\n" + "or even if the blood bank is supported properly. Every three seconds, " + "\n" + "somebody needs blood. One danation can save up to three lives!") 
      record = input("A small action can make a big change. Start it off! What would you like to do?")
      journal.append(record)    
  print("The big change is waiting" + "\n" + "Your actions to do:" + "\n" +str(journal))

  cont = input("Your action is listed. Would like to know more? Yes or no")
  if (cont == "Yes" or cont == "yes"):
      start = input("What would you like to know about? Littering, Speed driving, the Homeless, or Blood shortage?")
      if (start == "Littering" or start == "littering"):
          print("The amounts of liter in you community could be small. But the impact os great." + "\n" +"Random wastes thrown can clog strom water drain. This causes floods in the" + "\n" + "community, and the water does not always drain quickly.")
          record = input("A small action can make a big change. Start it off! What would you like to do?")
          journal.append(record)
      
      if (start == "Speed driving" or start == "speed driving" or start == "Speed Driving"):
          print("A community is small, but there are speed limits. They need" + "\n" + "to be strictly followed because it is not only you, but other cars, " + "\n" + "and people will be on the road." + "\n" + "Accidents can happen anytime, anywhere." + "\n" + "Every victim has family waiting for them.")
          record = input("A small action can make a big change. Start it off! What would you like to do?")
          journal.append(record)
      
      if (start == "the Homeless" or start == "The Homeless" or start == "the homeless"):
          print("Homes are lost everyday. Without a shelter, security, and proper resources, hundreds of thousands,553,742 people in the US, to be presice, are roaming on the streets.")
          record = input("A small action can make a big change. Start it off! What would you like to do?")
          journal.append(record)
            
      if (start == "Blood Shortage" or start == "blood shortage" or start == "Blood shortage"):
          print("A parent's hard skips a beat, when they heard that their child" + "\n" + "is short of blood. It is not guaranteed that the correct blood group will be found" + "\n" + "or even if the blood bank is supported properly. Every three seconds, " + "\n" + "somebody needs blood. One danation can save up to three lives!") 
          record = input("A small action can make a big change. Start it off! What would you like to do?")
          journal.append(record)
      print(journal)
  else:
      print("All done!")
      print("Your community is important. Make it better, and better.") 
      
#############End

##########Word Study
def studyword():
    import random
    number = int(input("Enter the number of terms you have: "))
    if (number < 1):
        print ("Try Again")
    else:
        words = []
        defins = []
        for i in range (number):
            word = input("Enter the word: ")
            words.append(word)
            defin = input("Enter the definition: ")
            defins.append(defin)
        #------------------------------------------------------------------
        clear ()
        print ("All words stored! Start testing.")
        copywords = words
        copydefins = defins
        right = []
        wrong = []
        rightCount = 0
        wrongCount = 0
        for i in range (number):
            num = random.randint(0,number - 1 - i)
            Ques = copydefins [num]
            Ans = input(Ques + ": ")
            if (Ans == copywords [num]):
                print ("Correct!")
                rightCount = rightCount + 1
                right.append(copywords [num])
            else:
                print ("Incorrect. The correct answer is " + copywords [num])
                wrongCount = wrongCount + 1
                wrong.append(copywords [num])
            copydefins.pop (num)
            copywords.pop (num)
        print ("You got " +  str(rightCount) + " answer(s) right:")
        print (*right, sep = "\n") 
        print ("You got " + str(wrongCount) + " answer(s) wrong:")
        print (*wrong, sep = "\n") 


#####TICTACTOE
def tictactoe():
  def display(gridlist):
      for x in range(0,7,3):
          for i in range(0,3,1):
              if i!=2:
                  print(gridlist[x+i], end="|")
              else:
                  print(gridlist[x+i], end=" ")
          print()
  def turn(remainingblocks, gridlist):
              number=int(input("Player 1, enter a number to place X"))
              if remainingblocks[number-1]==" ":
                  print("That is taken! Try again")
              else:
                  gridlist[number-1]="X"
                  remainingblocks[number-1]=" "

              
              
  def analyze(gridlist,remainingblocks,xtrap, cornertrap, inverttrap, ltrap, boottrap):
    def block(gridlist):
      ##Horizontal check
      for x in range(0,7,3):
          winlist=[]
          for i in range(0,3,1):
              winlist.append(gridlist[x+i])
          countx=winlist.count("X")
          if countx==2:
            for i in range(0,3,1):
              if winlist[i]!="X" and winlist[i]!="O":
                return i+x

      ##VERTICAL CHECK
      for x in range(0,3,1):
          winlist=[]
          for i in range(0,7,3):
              winlist.append(gridlist[x+i])
          countx=winlist.count("X")
          if countx==2:
              for z in range(0,3,1):
                  if winlist[z]!="X" and winlist[z]!="O":
                      return (z*3)+x
      ##Diagonal check my mom
      winlist=[]
      for x in range(0,9,4):
          winlist.append(gridlist[x])
      countx=winlist.count("X")
      if countx==2:
          for i in range(0,3,1):
              if winlist[i]!="X" and winlist[i]!="O":
                  return i*4
      winlist=[]
      for x in range(1,8,2):
          winlist.append(gridlist[x])
      countx=winlist.count("X")
      if countx==2:
          counter=2
          for i in range(0,3,1):
              if winlist[i]!="X" and winlist[i]!="O":
                  return counter
              counter+=2
      return "none"


    blockposition=block(gridlist)
  ###FIND OTHER PERSONS TRAP THEN block it
    if blockposition=="none":
        while True:
          randomindex=random.randint(0,8)
          if remainingblocks[randomindex]!=" ":
              gridlist[randomindex]="O"
              remainingblocks[randomindex]=" "
              break

    else:
      gridlist[blockposition]="O"
      remainingblocks[blockposition]=" "

              ##RETURN turn1
  def win(gridlist):
      ##Horizontal check
      for x in range(0,7,3):
          winlist=[]
          for i in range(0,3,1):
              winlist.append(gridlist[x+i])
          countx=winlist.count("X")
          county=winlist.count("O")
          if countx==3 or county==3:
              winner=True
              return winner
      ##VERTICAL CHECK
      for x in range(0,3,1):
          winlist=[]
          for i in range(0,7,3):
              winlist.append(gridlist[x+i])
          countx=winlist.count("X")
          county=winlist.count("O")
          if countx==3 or county==3:
              winner=True
              return winner   
      ##Diagonal check my mom
      winlist=[]
      for i in range(0,9,4):
          winlist.append(gridlist[i])
      countx=winlist.count("X")
      county=winlist.count("O")
      if countx==3 or county==3:
          winner=True
          return winner

      winlist=[]
      for i in range(1,8,2):
          winlist.append(gridlist[i])
      countx=winlist.count("X")
      county=winlist.count("O")
      if countx==3 or county==3:
          winner=True
          return winner
      winner=False
      return winner
          
              
  def start():
      ##VARIABLES AND DEFINITIONS
      gridlist=[1, 2, 3, 4, 5, 6, 7, 8, 9]
      remainingblocks=[1, 2, 3, 4, 5, 6, 7, 8, 9]
      ##TRAPS
      #PRIority
      xtrap=[ [2,[4,6,8],[0,2,7] ], [2,[0,4,6],[2,3,8]], [2,[0,2,4],[1,6,8]], [2,[2,4,8],[0,5,6]] ]
      
      cornertrap=[ [1,[0,6,8],[3,7]], [1,[0,2,6],[1,3]], [1,[0,2,8],[1,5]], [1,[2,6,8],[5,7]] ]
      #Priority
      inverttrap=[ [2,[3,4,6],[0,2,5]], [2,[0,3,4],[5,6,8]], [2,[2,4,5],[3,6,8]], [2,[4,5,8],[0,2,3]] ]
      
      ltrap=[ [1,[3,6,7],[0,8]],[1,[0,1,3],[2,6]],[1,[1,2,5],[0,8]],[1,[5,7,8],[2,6]] ]
      
      boottrap=[ [2,[0,6,7],[3,8]],[2,[0,2,3],[1,6]],[2,[1,2,8],[0,5]],[2,[5,6,8],[2,7]] ]

      
      print("Hello. Wanna play some tic tac toe?")
      winner=False
      while winner==False and remainingblocks.count(" ")!=9:
        counter=0
        display(gridlist)
        turn(remainingblocks, gridlist)
        winner=win(gridlist)
        counter+=1
        if winner==True:
          brea
        counter+=1
        analyze(gridlist, remainingblocks, xtrap, cornertrap, inverttrap, ltrap, boottrap)
        winner=win(gridlist)
      
      
      display(gridlist)
      if remainingblocks.count(" ")==9 and winner==False:
      ##TIED
          print("Tie!")
      elif counter%2!=0:
          print("Congrats player 1 you have won the game!")
      elif (counter%2)==0:
        print("Congrats! Computer won")
  start()
    














while True:
  print("Hi! Welcome to our Cryptohacks Smart Hub!")
  function = input("What would you like to do?\n A game of Hangman?\n Block Run?\n Calculator?\n Some Fun Jokes?\n WordStudy?\n Better Community?\n\n\n\n\n")
  function = function.lower()
  if (function == "calculator"):
    clear()
    calculator()
    continue

  if (function == "hangman" or function == "hang man"):
    clear()
    hangman()
    continue
  if (function == "wordstudy"):
    clear()
    studyword()
    continue
  if(function == "block run" or function == "blockrun"):
    clear()
    print("Copy - Paste this link into your search bar!")
    print("https://simmer.io/@Tbsr76/cube-runner-cryptohacks-2020")
    continue
  if (function == "better community" or function == "bettercommunity"):
    clear()
    bettercommunity()
    continue
  if(function == "fun jokes" or function == "jokes"):
    clear()
    fun_jokes()
    continue
