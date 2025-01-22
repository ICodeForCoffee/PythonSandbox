from SudokuSolver import SudokuSolver

def main():
    instance = SudokuSolver()
    puzzle = instance.load_puzzle("SudokuPuzzles\\sudoku-puzzle6.txt")
    
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