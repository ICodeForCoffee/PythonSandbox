# Roll for an ability score
import matplotlib.pyplot as plt
import numpy as np

def main():
    dice_results = {}
    
    for roll in range(3, 19):
        dice_results[roll] = 0
        
    for dice1 in range(1, 7):
        for dice2 in range(1, 7):
            for dice3 in range(1, 7):
                for dice4 in range(1, 7):
                    smallest_dice = min(dice1, dice2, dice3, dice4)
                    result = dice1 + dice2 + dice3 + dice4 - smallest_dice
                    dice_results[result] += 1
    
    display_ability_score_range(dice_results)

def display_ability_score_range(dice_results):
    xaxis = np.array([])
    yaxis = np.array([])
    
    for roll in range(3, 19):
        xaxis = np.append(xaxis, roll)
        yaxis = np.append(yaxis, dice_results[roll])
    
    plt.bar(xaxis, yaxis)
    plt.xlabel("Ability Score")
    plt.ylabel("Occurance")
    plt.title("Ability Score Range")
    plt.show()

main()