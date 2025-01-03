# Assumptions
# I calcualte that rolling with advantage gives you a boost 47.5% of the time.
# Some people say advantage is equivalent to a +5 boost, but we'll see what it calcualtes out to.
import numpy as np

def main():
    times_to_test = 1000000
    times_advantage_helped = 0
    improvement_total = 0
    difference_total = 0
    
    for x in range(times_to_test):
        advantage_helped, improvement, difference = calculate_advantage()
        difference_total += difference
        if (advantage_helped):
            times_advantage_helped += 1
            improvement_total += improvement
    
    if times_advantage_helped: 
        precent_rolls_improved = times_advantage_helped / times_to_test * 100
        advantage_improved_by = improvement_total/times_to_test
        advantage_improved_rolls_it_helped_by = improvement_total/times_advantage_helped
    else:
        precent_rolls_improved = 0
        advantage_improved_by = 0
        advantage_improved_rolls_it_helped_by = 0
        
    difference_between_rolls = difference_total/times_to_test
    
    print(f"We rolled for advantage {times_to_test:,} times\n")
    print(f"Advantaged improved our results {precent_rolls_improved:.2f}% of the time")
    print(f"Across all rolls we saw a +{advantage_improved_by:.2f} to rolls")
    print(f"Across rolls were advantage helped we saw a +{advantage_improved_rolls_it_helped_by:.2f} to rolls\n")
    print(f"However, if we treat the dice rolls as concurrent the average difference between the two dice is {difference_between_rolls:.2f}")
    
def calculate_advantage():
    roll1 = np.random.randint(1, 21)
    roll2 = np.random.randint(1, 21)
    advantage_helped = False
    improvement = 0
    difference = abs(roll2 - roll1)
    
    if roll2 > roll1:
        advantage_helped = True
        improvement = roll2 - roll1
    
    return advantage_helped, improvement, difference

main()