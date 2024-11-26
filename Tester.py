# Experimental tester for the Monty Hall Problem
import numpy as np

def main():
    count = int(input("How many iterations do you want to run? "))
    
    times_worth_changing = 0
    show_display = count <= 100
    
    for x in range(count):
        if run_porblem(show_display) == False:
            times_worth_changing += 1
            
    
    percentage = times_worth_changing / count * 100
    print()
    print(f"Out of those {count} iterations, changing doors gets you the prize {times_worth_changing} times")
    print(f"That is {percentage}%")
    return()

def run_porblem(show_display):
    door_with_prize = np.random.randint(1,4)
    door_selectted = np.random.randint(1,4)
    
    if(show_display):
        print("Selected door", door_selectted)
        print("The prize is behond", door_with_prize)
        print()
    
    if door_selectted == door_with_prize:
        return(True)
    else:
        return(False)

main()