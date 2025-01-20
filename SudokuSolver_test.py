from SudokuSolver import SudokuSolver
from SudokuPuzzle import SudokuPuzzle
import pytest

def test_basic_solving():
    puzzle = SudokuPuzzle()
    
    # The missing value here is 6.
    matrix = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, ' ', 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    
    for x in range(9):
        for y in range(9):
            puzzle.squares[x][y]['value'] = matrix[x][y]

    assert puzzle.is_solved() == False
    puzzle = SudokuSolver.solve_puzzle(puzzle)
    assert puzzle.squares[3][4]['value'] == 6
    assert puzzle.is_solved() == True

    matrix = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, ' ', 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    
    for x in range(9):
        for y in range(9):
            puzzle.squares[x][y]['value'] = matrix[x][y]

def test_simple_solving():
    puzzle = SudokuPuzzle()
    
    #This is the same Matrix from sudoku-puzzle1.txt    
    matrix = [
        [' ',' ', 2 , 7 ,' ',' ', 1 , 5 , 6 ],
        [' ', 3 ,' ', 6 , 2 , 8 ,' ', 4 ,' '],
        [ 7 , 6 , 9 ,' ',' ',' ',' ', 3 ,' '],
        [ 9 ,' ', 7 ,' ', 4 , 5 , 3 ,' ',' '],
        [' ',' ',' ',' ', 8 ,' ', 7 , 2 ,' '],
        [ 6 , 2 ,' ', 3 ,' ',' ', 5 ,' ',' '],
        [' ', 5 ,' ', 1 ,' ', 3 ,' ',' ', 9 ],
        [' ', 7 ,' ',' ', 9 ,' ', 2 ,' ', 5 ],
        [ 4 ,' ', 1 , 5 , 7 ,' ',' ',' ',' ']
    ]
    
    for x in range(9):
        for y in range(9):
            puzzle.squares[x][y]['value'] = matrix[x][y]

    
    assert puzzle.is_solved() == False
    puzzle = SudokuSolver.solve_puzzle(puzzle)
    assert puzzle.is_solved() == True
    assert puzzle.guessing_used == False

def test_load_function():
    puzzle = SudokuPuzzle()
    
    puzzle = SudokuSolver.load_puzzle("sudoku-puzzle1.txt")
    
    #This is the same Matrix from sudoku-puzzle1.txt    
    matrix = [
        [' ',' ', 2 , 7 ,' ',' ', 1 , 5 , 6 ],
        [' ', 3 ,' ', 6 , 2 , 8 ,' ', 4 ,' '],
        [ 7 , 6 , 9 ,' ',' ',' ',' ', 3 ,' '],
        [ 9 ,' ', 7 ,' ', 4 , 5 , 3 ,' ',' '],
        [' ',' ',' ',' ', 8 ,' ', 7 , 2 ,' '],
        [ 6 , 2 ,' ', 3 ,' ',' ', 5 ,' ',' '],
        [' ', 5 ,' ', 1 ,' ', 3 ,' ',' ', 9 ],
        [' ', 7 ,' ',' ', 9 ,' ', 2 ,' ', 5 ],
        [ 4 ,' ', 1 , 5 , 7 ,' ',' ',' ',' ']
    ]
    
    for x in range(9):
        for y in range(9):
            if isinstance(matrix[x][y], int) == True:
                assert int(puzzle.squares[x][y]['value']) == matrix[x][y]
            else:
                assert puzzle.squares[x][y]['value'] == matrix[x][y]