from SudokuSolver import SudokuSolver
import argparse
import time

def main():
    parser = argparse.ArgumentParser(prog="Sudoku Solver", description="Sudoku Solver")
    parser.add_argument("-file", help="Sudoku problem to solve", required=True, type=str)
    args = parser.parse_args()
    
    instance = SudokuSolver()
    puzzle = instance.load_puzzle(args.file)
    
    print("Initial puzzle\n")
    instance.display_puzzle(puzzle)
    
    start_time = time.time()
    puzzle = instance.solve_puzzle(puzzle)
    end_time = time.time()
    
    print("After attempting to solve\n")
    instance.display_puzzle(puzzle)
    
    print(f"This puzzle is {"solved" if puzzle.is_solved() == True else "unsolved"}")
    if __debug__:
        print()
        if puzzle.guessing_used == True:
            print(f"Guessing was used to calculate this result")
        if puzzle.analysis_helped == True:
            print("The analysis method helped")
        time_elapsed = end_time - start_time
        print()
        print(f"The solving method took {time_elapsed:.5f} seconds.")
    print()

main()