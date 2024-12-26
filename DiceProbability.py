# Roll 2 dice and graph the results.
import numpy as np

def main():
    dice_to_roll = get_input()
    total_sum = 0
    
    for count in range(dice_to_roll):
        dice1 = np.random.randint(1, 7)
        dice2 = np.random.randint(1, 7)
        roll = dice1 + dice2
        total_sum += roll

    average = total_sum/dice_to_roll
    print(f"The average of all the dice rolls is {average}")
    
def get_input():
    #I'm debating still if there will be an input on this one or we'll just graph it.
    return 100

main()