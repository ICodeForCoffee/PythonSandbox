import time
import numpy as np

def main():
    timer_tool(100)
    timer_tool(100)
    timer_tool(1000)
    timer_tool(1000000)

def timer_tool(total_rolls):
    print(f"to prefer {total_rolls:,d} dice rolls")

    start_vectorization = time.time()
    dice_rolls = np.random.randint(1, 7, size=(total_rolls))
    end_vectorization = time.time()
    time_for_vecrtorization = end_vectorization - start_vectorization

    print(f"It took {time_for_vecrtorization:.5f} seconds for vectorization to do all the dice rolls")

    start_for_loop = time.time()
    dice_rolls_for_loop = np.array([])
    for roll in range(total_rolls):
        np.append(dice_rolls_for_loop, np.random.randint(1, 7) )
    end_for_loop = time.time()

    time_for_vecrtorization = end_for_loop - start_for_loop

    print(f"It took {time_for_vecrtorization:.5f} seconds for the loop to do all the dice rolls\n")

main()