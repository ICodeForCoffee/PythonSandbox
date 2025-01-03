# Graphs the 400 possible outcomes of rolling two d20s
# The results this generates though aren't that interesting.
import matplotlib.pyplot as plt
import numpy as np

def main():
    dice_results = {}
    dice_improvement = {}
    
    # Let's get our results and then put them in.
    for roll in range(1, 21):
        dice_results[roll] = 0
        
    for roll in range(0, 20):
        dice_improvement[roll] = 0

    for dice1 in range(1, 21):
        for dice2 in range(1, 21):
            result = max(dice1, dice2)
            difference = abs(dice1 - dice2)
            
            dice_results[result] += 1
            dice_improvement[difference] += 1
            
    display_roll_results(dice_results)
    display_roll_improvement(dice_improvement)


def display_roll_results(dice_results):
    xaxis = np.array([])
    yaxis = np.array([])
    
    for roll in range(1, 21):
        xaxis = np.append(xaxis, roll)
        yaxis = np.append(yaxis, dice_results[roll])
    
    plt.bar(xaxis, yaxis)
    plt.xlabel("Dice Result")
    plt.xlabel("Occurrence")
    plt.title("Possible results for rolling two d20s")
    plt.show()
    
def display_roll_improvement(dice_improvement):
    xaxis = np.array([])
    yaxis = np.array([])
    
    for roll in range(0, 20):
        xaxis = np.append(xaxis, roll)
        yaxis = np.append(yaxis, dice_improvement[roll])
    
    plt.bar(xaxis, yaxis)
    plt.xlabel("Imprement Result")
    plt.xlabel("Occurrence")
    plt.title("If we roll dice concurrently, we should see the following improvement between the two dice")
    plt.show()

main()