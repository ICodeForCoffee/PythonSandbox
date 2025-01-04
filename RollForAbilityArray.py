# Generates ability scores for a character in D&D and compares the average of the results to the standard array.
# Roll for an ability score
import matplotlib.pyplot as plt
import numpy as np

def main():
    dice_sum = {}
    total_rolls = 10000
    
    for roll in range(1, 7):
        dice_sum[roll] = 0
    
    for count in range(total_rolls):
        dice_results=[get_ability_score(), get_ability_score(), get_ability_score(), get_ability_score(),
                      get_ability_score(),get_ability_score(), get_ability_score()]
        dice_results = sorted(dice_results, reverse=True )

        dice_sum[1] += dice_results[0]
        dice_sum[2] += dice_results[1]
        dice_sum[3] += dice_results[2]
        dice_sum[4] += dice_results[3]
        dice_sum[5] += dice_results[4]
        dice_sum[6] += dice_results[5]
    
    average_array = [dice_sum[1] / total_rolls, 
                     dice_sum[2] / total_rolls,
                     dice_sum[3] / total_rolls,
                     dice_sum[4] / total_rolls,
                     dice_sum[5] / total_rolls,
                     dice_sum[6] / total_rolls]
    
    display_ability_score_range(average_array)

def get_ability_score():
    dice1 = np.random.randint(1, 7)
    dice2 = np.random.randint(1, 7)
    dice3 = np.random.randint(1, 7)
    dice4 = np.random.randint(1, 7)
    
    low_roll = min(dice1, dice2, dice3, dice4)
    result = dice1 + dice2 + dice3 + dice4 - low_roll
                    
    return result

def display_ability_score_range(dice_results):
    xaxis = np.array([])
    yaxis = np.array([])
    
    standard_array = ([15, 14, 13, 12, 10, 8])
    
    plt.plot(dice_results)
    plt.plot(standard_array)
    plt.xlabel("Ability Score")
    plt.ylabel("Occurance")
    plt.title("Ability Score Rolled vs Standard Array")
    plt.show()

main()