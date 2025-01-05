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
    dice_rolls = np.random.randint(1, 7, size=(2, total_rolls))
    dice_totals = np.sum(dice_rolls, axis=0)
    unique, counts = np.unique(dice_totals, return_counts=True)
    dice_results = dict(zip(unique, counts))

    # Insert missing values into the dictionary
    for roll in range(2, 13):
        if dice_results.get(roll) == None:
            dice_results[roll] = 0
    
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