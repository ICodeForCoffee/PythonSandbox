from SudokuSolver import SudokuSolver
import argparse

def main():
    parser = argparse.ArgumentParser(prog="Sudoku Solver", description="Sudoku Solver")
    parser.add_argument("-file", help="Sudoku problem to solve", required=True, type=str)
    args = parser.parse_args()
    
    instance = SudokuSolver()
    puzzle = instance.load_puzzle(args.file)
    
    print("Initial puzzle\n")
    instance.display_puzzle(puzzle)
    puzzle = instance.solve_puzzle(puzzle)
    print("After attempting to solve\n")
    instance.display_puzzle(puzzle)
    print(f"This puzzle is {"solved" if puzzle.is_solved() == True else "unsolved"}")
    if puzzle.guessing_used == True:
        print(f"Guessing was used to calculate this result")
    print()

main()