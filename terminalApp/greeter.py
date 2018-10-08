from time import sleep
import os

#Terminal application greets old friends and remembers new friends

#Display a title bar
def display_title_bar(): 
  #clear terminal screen, and display title bar
  os.system('clear')

  print ("\t**********************************************")
  print("\t***  Greeter - Hello old and new friends!  ***")
  print("\t**********************************************")


#Print a bunch of information, in short intervals
names = ['aaron', 'brenda', 'cyrene', 'david', 'eric']

#print each name 5 times. 
for name in names: 
  display_title_bar()

  print("\n\n")
  for x in range(0,5):
    print(name.title())

  #pause for 1 second between batches
  sleep(1)
