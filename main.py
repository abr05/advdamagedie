## calculate adv on any die damage rolls ##

import random
total=0
i=0
dice=int(input("Enter how many dice to roll:\n"))
size=int(input("Enter damage die size:\n"))

for num in range(dice):
  die1=(random.randint(1,size))
  print ("\nDice 1 roll:", die1)
  die2=(random.randint(1,size))
  print ("Dice 2 roll:", die2)
# sanity check dice counter:
  i=i+1
# loop to give advantage

  if (die1 > die2):
    total +=die1
    print ("\nDie " + str(i) +" Advantage: " + str(die1) + "\nRunning Total:", total)
  elif (die2 > die1):
    total +=die2
    print ("\nDie " + str(i) +" Advantage: " + str(die2) + "\nRunning Total:", total)
  else:
    total +=die2
    print ("\nDie " + str(i) +" Advantage: " + str(die2) + "\nRunning Total:", total)

print ("\nTotal:" + str(total))
