# Assumptions
# I calcualte that rolling with advantage gives you a boost 47.5% of the time.
# Some people say advantage is equivalent to a +5 boost, but we'll see what it calcualtes out to.
import numpy as np

def main():
    times_to_test = 1000000
    times_advantage_helped = 0
    improvement_total = 0
    silly_hundred = 100
    
    for count in range(times_to_test):
        advantage_helped, improvement = calculate_advantage()
        if (advantage_helped):
            times_advantage_helped += 1
            improvement_total += improvement
    
    precent_rolls_improved = 0
    advantaged_improved = 0
    advantaged_improved_rolls_it_helped_by = 0
    
    if times_advantage_helped: 
        precent_rolls_improved = times_advantage_helped / times_to_test * 100
        advantaged_improved = improvement_total/times_to_test
        advantaged_improved_rolls_it_helped_by = improvement_total/times_advantage_helped
    
    print(f"We rolled for advantage {times_to_test:,} times\n")
    print(f"Advantaged improved our results {precent_rolls_improved:.2f}% of the time")
    print(f"Across all rolls we saw a +{advantaged_improved:.2f} to rolls")
    print(f"Across rolls were advantage helped we saw a +{advantaged_improved_rolls_it_helped_by:.2f} to rolls")
    
def calculate_advantage():
    roll1 = np.random.randint(1, 21)
    roll2 = np.random.randint(1, 21)
    advantage_helped = False
    improvement = 0
    
    if roll2 > roll1:
        advantage_helped = True
        improvement = roll2 - roll1
    
    return advantage_helped, improvement

main()