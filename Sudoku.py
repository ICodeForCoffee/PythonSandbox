import numpy

from SudokuSolver import SudokuSolver


def main():
    puzzle = SudokuSolver.load_puzzle("sudoku-puzzle5.txt")
    print("Initial puzzle\n")
    SudokuSolver.display_puzzle(puzzle)
    puzzle = SudokuSolver.solve_puzzle(puzzle)
    print("After attempting to solve\n")
    SudokuSolver.display_puzzle(puzzle)
    print(f"This puzzle is {"solved" if puzzle.is_solved() == True else "unsolved"}")
    print()

main()