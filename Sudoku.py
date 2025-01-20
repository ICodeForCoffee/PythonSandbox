from SudokuSolver import SudokuSolver

def main():
    puzzle = SudokuSolver.load_puzzle("SudokuPuzzles\sudoku-puzzle4.txt")
    print("Initial puzzle\n")
    SudokuSolver.display_puzzle(puzzle)
    puzzle = SudokuSolver.solve_puzzle(puzzle)
    print("After attempting to solve\n")
    SudokuSolver.display_puzzle(puzzle)
    print(f"This puzzle is {"solved" if puzzle.is_solved() == True else "unsolved"}")
    if puzzle.guessing_used == True:
        print(f"Guessing was used to calculate this result")
    print()

main()