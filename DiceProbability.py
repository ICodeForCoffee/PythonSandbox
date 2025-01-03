# Roll 2 dice and graph the results.
import matplotlib.pyplot as plt
import numpy as np

def main():
    calculate_dice_rolls(10)
    calculate_dice_rolls(100)
    calculate_dice_rolls(1000)
    calculate_dice_rolls(10000)
    calculate_dice_rolls(100000)

def calculate_dice_rolls(total_rolls):
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
    
    for count in range(total_rolls):
        dice1 = np.random.randint(1, 7)
        dice2 = np.random.randint(1, 7)
        roll = dice1 + dice2
        total_sum += roll
        dice_results[roll] += 1

    average = total_sum/total_rolls
    display_results(dice_results, total_rolls)

def display_results(dice_results, total_rolls):
    xaxis = np.array([])
    yaxis = np.array([])
    
    for roll in range(2, 13):
        xaxis = np.append(xaxis, roll)
        yaxis = np.append(yaxis, dice_results[roll])
    
    plt.bar(xaxis, yaxis)
    plt.xlabel("Dice Result")
    plt.title(f"Result for {total_rolls:,} rolls")
    plt.show()

main()