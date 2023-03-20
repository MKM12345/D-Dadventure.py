import colorama
from colorama import Fore    

print(Fore.RED)              # RED COLOUR TEXT
print(' ')                  # A line break
print('****Welcome to Dungeons & Dragons****')
print(' ')
print("Your Dungon Master today will be me - Mantra Jhala")
print(' ')
print(Fore.WHITE) 
print("You are standing on a pathway in the countryside with your guild.")
print(' ')
print("Suddenly, a trio of orcs rush you from a nearby bush! What do you do ?")
print(' ')
print(Fore.GREEN)            # GREEN COLOUR TEXT
print("You have 2 choices. They are: 1 - Throw your hand axes at the orcs OR 2 - Send a spell at the orcs? : - ")
print(' ')
print(Fore.BLUE)             # BLUE COLOUR TEXT

dnd_choice = input("Please enter either 1 or 2 as your choice here :- ")
if dnd_choice == "1": # Run from bush 
  # This code is indented 1 time because it is 1 choice deep
  print(Fore.GREEN)
  print(' ')
  print("You threw hand axes however, the Orcs did not die and now Orcs are coming to attack you!")
  print(' ')
  print(Fore.BLUE)             # BLUE COLOUR TEXT
  damage_choice = input("Do you 1. Disengage or 2. Tank the hit: - ")

  if damage_choice == "1": # Powerful hit, die
    # This code is indented 2 time because it is 2 choices deep
    print(Fore.GREEN)            # GREEN COLOUR TEXT
    print(' ')  
    print("You disapper and appear again, 60 feet away.  The Orcs clumsily trip over each other and fall. You have disengaged, now you have 2 choices")
    print(' ')
    print(Fore.BLUE)             # BLUE COLOUR TEXT
    disengage_choice = input("Do you 1. Run back into combat or 2. Let your friends have a shot and then run back in: - ")

    if disengage_choice == "1": 
    # This code is indented 3 time because it is 3 choices deep
      print(Fore.GREEN)            # GREEN COLOUR TEXT
      print(' ')      
      print("The Orcs glare at you, when you run for the combat and strike you with their maul. You take too much damage & you Die")
      print("GAME OVER")
      
    elif disengage_choice == "2":
     # This code is indented 3 time because it is 3 choices deep 
      print(Fore.GREEN)            # GREEN COLOUR TEXT
      print(' ')
      print("The Artificer's dragon, Kamiyami strikes the orcs with bolts of lightning and kills them.")
      print("You see light through the trees and escape from the battle field, unhurt!")
      print("YOU WIN")

    elif disengage_choice != "1" or "2": # Check choices using logical operator (or) 
      print(' ')
      print("Incorrect input, please restart game")

    
  elif damage_choice == "2":
  # This code is indented 2 time because it is returning back to 2nd level else if
    print(Fore.GREEN)            # GREEN COLOUR TEXT
    print(' ')
    print("The Orcs simultaneously, smash you into a pancake with their mauls. You died. ")
    print("GAME OVER")

  elif damage_choice != "1" or "2": # Check choices using logical operator (or) 
    print(' ')
    print("Incorrect input, please restart game")
   
elif dnd_choice == "2":
# This code is indented 1 time because it is returning back to 1st level else if
  print(Fore.GREEN)            # GREEN COLOUR TEXT
  print(' ')
  print("You launch a kinetic blast so powerful it sends an orcs head hurtling away. The other 2 orcs are very angry, and so they smash Kamiyami into the floor. He is now on death saves. You have one potion of healing left. Do you either 1. Heal Kamiyami or 2. Only perform a medicine check on him.")
  print(' ')
  print(Fore.BLUE)             # BLUE COLOUR TEXT
  healing_choice = input("Do you 1. Heal Kamiyami or 2. Only perform a medicine check on him: - ")
  
  if healing_choice == "1": 
    print(' ')
    print("GAME OVER - Kamiyami comes back to life and shoots bolts of lightning at the orcs and they die.  You Win.")
    
  elif healing_choice == "2":
    print(' ')
    print("GAME OVER - You tried to perform the medicine check, but you panic and poke the wound and make it worst. Kamiyami dies, orcs attack you, you take too much damage & die.")

  elif healing_choice != "1" or "2": # Check choices using logical operator (or) 
    print(' ')
    print("Incorrect input, please restart game")

elif dnd_choice != "1" or "2": # Check choices using logical operator (or) 
  print(' ')
  print("Incorrect input, please restart game")

