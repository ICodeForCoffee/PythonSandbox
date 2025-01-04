# Graphs the 400 possible outcomes of rolling two d20s.
import matplotlib.pyplot as plt
import numpy as np

def main():
    dice_results = {}
    dice_improvement_rolled_seperately = {}
    dice_improvement_rolled_concurrent = {}
    
    # Let's get all the possible dice combinations and then put them in a dictionary.
    for roll in range(1, 21):
        dice_results[roll] = 0
        
    for roll in range(0, 20):
        dice_improvement_rolled_seperately[roll] = 0
        dice_improvement_rolled_concurrent[roll] = 0

    for dice1 in range(1, 21):
        for dice2 in range(1, 21):
            result = max(dice1, dice2)
            difference = abs(dice1 - dice2)
            
            dice_results[result] += 1
            
            if(dice2 > dice1):
                dice_improvement_rolled_seperately[difference] += 1
            else:
                dice_improvement_rolled_seperately[0] += 1
            
            dice_improvement_rolled_concurrent[difference] += 1
    
    display_roll_results(dice_results)
    display_roll_improvement(dice_improvement_rolled_seperately, "If we roll dice in order")
    display_roll_improvement(dice_improvement_rolled_concurrent, "If we roll dice concurrently")

def display_roll_results(dice_results):
    xaxis = np.array([])
    yaxis = np.array([])
    
    for roll in range(1, 21):
        xaxis = np.append(xaxis, roll)
        yaxis = np.append(yaxis, dice_results[roll])
    
    plt.bar(xaxis, yaxis)
    plt.xlabel("Dice Result")
    plt.ylabel("Occurrence")
    plt.title("Frequency of results for rolling with advantage")
    plt.show()
    
def display_roll_improvement(dice_improvement, title):
    xaxis = np.array([])
    yaxis = np.array([])
    
    for roll in range(0, 20):
        xaxis = np.append(xaxis, roll)
        yaxis = np.append(yaxis, dice_improvement[roll])
    
    plt.bar(xaxis, yaxis)
    plt.xlabel("Improvement by rolling with advantage")
    plt.ylabel("Occurance")
    plt.title(title)
    plt.show()

main()