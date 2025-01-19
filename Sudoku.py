from SudokuSolver import SudokuSolver

def main():
    puzzle = SudokuSolver.load_puzzle("sudoku-puzzle5.txt")
    print("Initial puzzle\n")
    SudokuSolver.display_puzzle(puzzle)
    puzzle, used_guessing = SudokuSolver.solve_puzzle(puzzle)
    print("After attempting to solve\n")
    SudokuSolver.display_puzzle(puzzle)
    print(f"This puzzle is {"solved" if puzzle.is_solved() == True else "unsolved"}")
    if used_guessing == True:
        print(f"Guessing was used to calculate this result")
    print()

main()