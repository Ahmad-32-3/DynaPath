from functions import max_height, horizontal_displacement, fixed_height, fixed_displacement, big_5
from moffat import clear, ask_clear, slow_print

# Introduction
slow_print("This is a physics calculator. It can calculate projectile motion as well as one dimensional motion pertaining to the big 5. This program utilizes the traditional positive rotation of a unit circle. So if you would like to tell the calculator the object in question is thrown down, you would need to convert that value as if you were in the fourth quadrant. For instance, if something is thrown forward, 20 degrees down, it would be forward 340 degrees. The user must use up as positive, downward vector quantities must be negative. ")
ask_clear()

# Initiates while loop 
while True: 

  # Asks user what they would like to find
  slow_print("""
  What would you like to find?\n
  1. Find the maximum height of a projectile\n
  2. Find the displacement of where the projectile lands from initial position.\n
  3. Find at what distance a container of [blank] height should be placed, such that the projectile lands inside the container. Or, find at what height a container of [blank] distance should be 
     placed such that the projectile lands inside the container(target problems)\n
  4. Solve a physics question using the big 5.\n
  5. Exit the program\n
  """)


  # While loop to catch invalid inputs
  while True:
    try:
      choice = int(input("\nEnter choice (1 to 5): "))
      if choice in [1,2,3,4,5]:
        break
      else:
        print("Invalid input, select numbers 1,2,3,4 or 5")
        continue
    except ValueError or choice not in [1,2,3,4,5]:
      print("Invalid input, select numbers 1,2,3,4 or 5")
      continue
  clear()
  
  # If statements to select each calculator
  if choice == 1:
    max_height()
  elif choice == 2:
    horizontal_displacement()
  elif choice == 3:
    
    # Asks user what type of problem they would like to solve
    slow_print("There are two types of problems. Select the type that is most applicable to you")
    slow_print("1. The container has a fixed height and you must find the distance from the initial launch point such that the projectile lands inside the container")
    slow_print("2. There is a fixed distance from the initial launch point and you must find the height at which the container must be put at such that the projectile lands inside it.")

    # While loop to catch invalid inputs
    while True:
      try:
        sub_choice = int(input("\nEnter choice (1 or 2): "))
        
        if sub_choice in [1,2]:
          break
        else:
          continue
          
      except ValueError:
        continue
        
    if sub_choice == 1:
      fixed_height()
    else:
      fixed_displacement()

  elif choice == 4:
    slow_print("\nNote that the user must select a direction as positive and input all values in accordance to that. For instance, if up is postiive than the acceleration due to gravity is negative.\nAlso, to indicate that you do not have a value in a question, simply press enter.")
    result, arg, names, units = big_5()
    print(f"The {names[arg]} is {result:.3f} {units[arg]}")
    
  elif choice == 5:
    slow_print("Thank you for using the projectile motion calculator!")
    break
    
  else:
    slow_print("Invalid input, please try again")
  ask_clear()

  