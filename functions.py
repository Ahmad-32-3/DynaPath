import math
from collections import defaultdict
import numpy as np

def get_inputs():
  """
  Prompt the user to enter inputs for a physics problem.

  Returns:
      defaultdict: A dictionary containing the input variables for the physics problem.
          The keys are strings representing the variable names, and the values are floats.
  """
  variables = defaultdict(float)
  
  while True:
    try:
      variables["mag_v"] = float(input("Please input the magnitude of the initial velocity(m/s)(DO NOT INCLUDE ANGLE): "))
      variables["angle"] = float(input("Please input the angle of the initial velocity relative to a traditional unit cirlce(degrees): "))
      variables["a"] = float(input("Enter the acceleration due to gravity(SHOULD BE A NEGATIVE IF YOU SELECT UP AS POSITIVE! On Earth the acceleration due to gravity is 9.81m/s^2[DOWN]): "))
      variables["di"] = float(input("Enter the initial displacement from ground(meters): "))
      if variables["a"] >= 0:
        print("The acceleration must be inputted as a negative number. Please select up as the positive direction. Acceleration also cannot be 0.\n")
        continue
      break
    except ValueError:
      print("\nInvalid input. Please enter numerical values.")

  return variables

def quadratic_formula(a,b,c):
  """
  Solve a quadratic equation using the quadratic formula.

  Args:
      a (float): Coefficient of the quadratic term.
      b (float): Coefficient of the linear term.
      c (float): Constant term.

  Returns:
      tuple: A tuple containing the two solutions of the quadratic equation.
  """
  t1, t2 = 0, 0
  try: 
    t1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    t2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
  except ValueError:
    print("Numbers are needed, not letters, please try again")
  return t1, t2
    
def eq1(variables, choice):
  """
    Solve for an unknown variable using the first equation of motion (kinematic equation).

    Args:
        variables (dict): A dictionary containing the variable values.
        choice (str): The unknown variable to solve for.

    Returns:
        float: The value of the unknown variable.

    """
  if choice == "d":
      return variables["vi"] * variables["t"] + 0.5 * variables["a"] * variables["t"] ** 2
  elif choice == "vi":
      return (variables["d"] - 0.5 * variables["a"] * variables["t"] ** 2) / variables["t"]
  elif choice == "a":
      return (2 * (variables["d"] - variables["v"] * variables["t"])) / variables["t"] ** 2
  elif choice == "t":
      ans1, ans2 = quadratic_formula (0.5*variables["a"], variables["vi"], variables["d"])
      return max(ans1, ans2)

def eq2(variables, choice):
  """
    Solve for an unknown variable using the second equation of motion (kinematic equation).

    Args:
        variables (dict): A dictionary containing the variable values.
        choice (str): The unknown variable to solve for.

    Returns:
        float: The value of the unknown variable.

    """
  if choice == "d":
      return variables["vf"] * variables["t"] - 0.5 * variables["a"] * variables["t"] ** 2
  elif choice == "a":
      return (-2 * (variables["d"] - variables["vf"] * variables["t"])) / variables["t"] ** 2
  elif choice == "vf":
      return (variables["d"] + 0.5 * variables["a"] * variables["t"] ** 2) / variables["t"]
  elif choice == "t":
      ans1, ans2 = quadratic_formula (0.5*variables["a"], variables["vi"], variables["d"])
      print(f"The time is {ans1:.3f} s")
      return ans2
    
def eq3(variables, choice):
  """
    Solve for an unknown variable using the third equation of motion (kinematic equation).

    Args:
        variables (dict): A dictionary containing the variable values.
        choice (str): The unknown variable to solve for.

    Returns:
        float: The value of the unknown variable.

    """
  if choice == "vf":
      return math.sqrt(variables["vi"] ** 2 + (2 * variables["a"] * variables["d"]))
  elif choice == "vi":
      return math.sqrt(variables["vf"] ** 2 - (2 * variables["a"] * variables["d"]))
  elif choice == "a":
      return (variables["vf"] ** 2 - variables["vi"] ** 2) / (2 * variables["d"])
  elif choice == "d":
      return (variables["vf"] ** 2 - variables["vi"] ** 2) / (2 * variables["a"])

def eq4(variables, choice):
  """
    Solve for an unknown variable using a variation of the fourth equation of motion (kinematic equation).

    Args:
        variables (dict): A dictionary containing the variable values.
        choice (str): The unknown variable to solve for.

    Returns:
        float: The value of the unknown variable.

    """
  if choice == "d":
      return (variables["vi"] * variables["t"])
  elif choice == "vi":
      return (variables["d"] / variables["t"])
  elif choice == "t":
      return (variables["d"] / variables ["vi"])

def eq5(variables, choice):
  """
    Solve for an unknown variable using the fifth equation of motion (kinematic equation).

    Args:
        variables (dict): A dictionary containing the variable values.
        choice (str): The unknown variable to solve for.

    Returns:
        float: The value of the unknown variable.

    """
  if choice == "vf":
      return variables["vi"] + variables["a"] * variables["t"]
  elif choice == "vi":
      return variables["vf"] - variables["a"] * variables["t"]
  elif choice == "a":
      return (variables["vf"] - variables["vi"]) / variables["t"]
  elif choice == "t":
      return (variables["vf"] - variables["vi"]) / variables["a"]
    
def eq6(variables, choice):
  """
    Solve for an unknown variable using the third equation of motion (kinematic equation).

    Args:
        variables (dict): A dictionary containing the variable values.
        choice (str): The unknown variable to solve for.

    Returns:
        float: The value of the unknown variable.

    """
  if choice == "d":
      return variables["vi"] * variables["t"] + 0.5 * variables["a"] * variables["t"] ** 2
  elif choice == "vi":
      return (variables["d"] - 0.5 * variables["a"] * variables["t"] ** 2) / variables["t"]
  elif choice == "a":
      return (2 * (variables["d"] - variables["v"] * variables["t"])) / variables["t"] ** 2
  elif choice == "t":
      ans1, ans2 = quadratic_formula (0.5*variables["a"], variables["vi"], variables["d"])
      print(f"The time is {ans1:.3f} s")
      return ans2
    
def eq7(variables, choice):
  """
    Solve for an unknown variable using the first equation of motion (kinematic equation).

    Args:
        variables (dict): A dictionary containing the variable values.
        choice (str): The unknown variable to solve for.

    Returns:
        float: The value of the unknown variable.
        
    """
  if choice == "d":
      return ((variables["vi"] + variables["vf"]) / 2) * variables["t"]
  elif choice == "vi":
      return ((2 * variables["d"]) / variables["t"]) - variables["vf"]
  elif choice == "vf":
      return (2 * variables["d"]) / variables["t"] - variables["vi"]
  elif choice == "t":
      return (2 * variables["d"] - variables["vi"]) / variables["vf"]
    
def max_height():
  """
    Calculates the maximum height of a projectile based on the given vector velocity quantities.

    Returns:
    The maximum height of the projectile in meters.
    
    """
  variables = get_inputs()
      
  # use trignometric ratios to solve for verticle component of velocity after angle is converted to degrees
  variables["vi"] = variables["mag_v"] * math.sin(np.radians(variables["angle"]))

  # Set final velocity to 0
  variables ["vf"] = 0
  
  # Calculate maxmimum height 
  if variables["angle"] == 0 or variables["angle"] >= 180 and variables["angle"]<=360:
    ans = variables["di"]
  else:
    ans = eq3(variables, "d") + variables["di"]

  # Output maximum height
  print(f"\nThe maximum height of the projectile is {ans:.3f} meters, remember to round to the correct significant figures given in the question.")
    
def horizontal_displacement():
  """
  Calculates the horizontal displacement of a projectile based on the given vector velocity quantities.
  
  Returns:
  The horizontal displacement from the initial launch position of the projectile in meters.
  """
  variables = get_inputs()

  variables["d"] = variables["di"]
# Convert initial velocity into horizontal and vertical components
  vi_x = variables["mag_v"] * math.cos(np.radians(variables["angle"]))
  vi_y = variables["mag_v"] * math.sin(np.radians(variables["angle"]))
  
  # Calculate time using eq1
  variables["vi"] = vi_y
  time = eq1(variables, "t")
  # Solve for horizontal displacement in eq4
  variables["vi"] = vi_x
  variables["t"] = time
  displacement = eq4(variables, "d")

  # Output answer
  print(f"\nThe displacement from the initial launch of the projectile is {displacement:.3f} meters, remember to round to the correct significant figures given in the question.")

def fixed_height():
  """
  Calculates the displacement from the initial launch position at which a container should be placed
  such that the projectile lands inside it, based on the given initial velocity and acceleration of the projectile.
  
  Returns:
  The horizontal displacement from the initial launch position of the projectile in meters.
  """
  variables = defaultdict(float)
  variables = get_inputs()
  # Takes inputs from user
  while True:
    try:
      variables["dc"] = float(input("Enter the fixed height of the container(meters): "))
      break
    except ValueError:
      print("\nInvalid input. Please enter numerical values.")
      continue
      
  # Convert initial velocity into horizontal and vertical components
  vi_x = variables["mag_v"] * math.cos(np.radians(variables["angle"]))
  vi_y = variables["mag_v"] * math.sin(np.radians(variables["angle"]))
  
  # Adjust displacement value
  variables["d"] = variables["di"] - variables["dc"]

  # Calculate time using eq1
  variables["vi"] = vi_y
  time = eq1(variables, "t")

  # Solve for horizontal displacement using eq4
  variables["vi"] = vi_x
  variables["t"] = time
  displacement = eq4(variables, "d")

  # Output answer
  print(f"\nThe horizontal displacement of the container/target from the initial launch of the projectile is {displacement:.3f} meters, remember to round to the correct significant figures given in the question.")

def fixed_displacement():
  """
  Calculates the height at which a container should be placed such that the projectile lands inside it,
  based on the given initial velocity and acceleration of the projectile.
  
  Returns:
  The height of the container in meters.
  """

  variables = defaultdict(float)
  variables = get_inputs()
  
  # Takes inputs from user
  while True:
    try:
      d_container = float(input("Enter the fixed displacement of the container(meters): "))
      break
    except ValueError:
      print("\nInvalid input. Please enter numerical values.")
      continue
      
  # Convert initial velocity into horizontal and vertical components
  vi_x = variables["mag_v"] * math.cos(np.radians(variables["angle"]))
  vi_y = variables["mag_v"] * math.sin(np.radians(variables["angle"]))

  # Use horizontal components to find time
  variables["vi"] = vi_x
  variables["d"] = d_container
  time = eq4(variables, "t")

# Use vertical componenets to find height
  variables["vi"] = vi_y
  variables["t"] = time
  height = eq1(variables, "d")

  # Adjust height from initial displacement
  adjusted_height = variables["di"] + height
  # Output answer
  print(f"\nThe height of the container/target should be {adjusted_height:.3f} meters, remember to round to the correct significant figures given in the question.")

def big_5():
  """
  Solves physics equations involving the "big 5" variables (a, vi, vf, t, d).
  
  Returns:
  A tuple containing the calculated value, the variable being solved for, a dictionary mapping variable codes
  to their corresponding names, and a dictionary mapping variable codes to their corresponding units.
  """
  variables = defaultdict(float)
  
  while True:

    # Asks user to input variables
      try:
          choice = input("What variable would you like to solve for(a, vi, vf, t, d): ")
      except ValueError:
          print("Invalid input, try again")
          continue
        
      if choice != "a":
          try:
              variables["a"] = float(input("What is acceleration?(m/s^2): "))
          except ValueError:
              unknown = "a"
        
      if choice != "t":
          try:
              variables["t"] = float(input("What is time?(s): "))
          except ValueError:
              unknown = "t"

      if choice != "vi":
          try:
              variables["vi"] = float(input("What is initial velocity?(m/s): "))
          except ValueError:
              unknown = "vi"
            
      if choice != "vf" and len(variables) < 3:
          try:
              variables["vf"] = float(input("What is final velocity?(m/s): "))
          except ValueError:
              unknown = "vf"
      elif choice != "vf":
        unknown = "vf"
      else:
        unknown = "d"
        
      if choice != "d" and len(variables) < 3:
          try:
              variables["d"] = float(input("What is displacement?(m): "))
          except ValueError:
              unknown = "d"
      elif choice != "d":
        unknown = "d"
            
      # Selects which equation to use depending on what variable is unknown
      if unknown == "vf":
          run = eq6(variables, choice)
      elif unknown == "vi":
          run = eq2(variables, choice)
      elif unknown == "t":
          run = eq3(variables, choice)
      elif unknown == "a":
          run = eq7(variables, choice)
      elif unknown == "d":
          run = eq5(variables, choice)
      break
    
  big_five_choices = {
  "a": "acceleration", 
  "vi": "initial velocity",
  "vf": "final velocity",
  "t": "time",
  "d": "displacement"
}
  big_five_units = {
  "a": "m/s^2",
  "vi": "m/s",
  "vf": "m/s",
  "t": "s",
  "d": "m"
}
  return run, choice, big_five_choices, big_five_units
