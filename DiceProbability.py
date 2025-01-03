# Roll 2 dice and graph the results.
import matplotlib.pyplot as plt
import numpy as np

def main():
    dice_to_roll = get_input()
    total_sum = 0
    
    dice_results = {
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
    }
    
    for count in range(dice_to_roll):
        dice1 = np.random.randint(1, 7)
        dice2 = np.random.randint(1, 7)
        roll = dice1 + dice2
        total_sum += roll
        dice_results[roll] += 1

    average = total_sum/dice_to_roll
    print(f"The average of all the dice rolls is {average}")
    display_results(dice_results)
    
def display_results(dice_results):
    xaxis = np.array([])
    yaxis = np.array([])
    
    for roll in range(2, 13):
        xaxis = np.append(xaxis, roll)
        yaxis = np.append(yaxis, dice_results[roll])
    
    plt.bar(xaxis, yaxis)
    plt.show()
    
def get_input():
    #I'm debating still if there will be an input on this one or we'll just graph it.
    return 10000

main()