import os
import time

def ask_clear():
    """Clears the console when the user is ready"""
    input("\n\nPress enter to continue(clears console of text)")
    os.system('clear')

def clear():
    """Immediately clears the console"""
    os.system('clear')

def slow_print(string,t=0.02):
    """Prints each character in the given string with a delay, creating a slow printing effect."""
    for item in string:
        print(item,end="", flush=True)
        time.sleep(t)
    print()