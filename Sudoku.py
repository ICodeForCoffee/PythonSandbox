import numpy


def main():
    puzzle = load_puzzle("sudoku-puzzle4.txt")
    print("Initial puzzle\n")
    display_puzzle(puzzle)
    solve_puzzle(puzzle)

def load_puzzle(fila_name):
    file = open(fila_name, "r")
    puzzle = SudokuPuzzle()
    
    for x in range(9):
        line = file.readline()
        line = line.replace("|", "")
        
        for y in range(9):
            puzzle.squares[x][y]['value'] = line[y]
        
        pass
    return puzzle

def display_puzzle(puzzle):
    for x in range(9):
        if x == 3 or x == 6:
            print("---------   ---------   ---------")
        for y in range(9):
            if y == 3 or y == 6:
                print(" | ", end="")
            print(f" {puzzle.squares[x][y]['value']} ", end="")
            
        print("")

def solve_puzzle(puzzle):
    changesd_squares = 1
    
    while changesd_squares > 0:
        changesd_squares = 0
        puzzle = populate_possible_values(puzzle)
        puzzle = prune_possibilities(puzzle)
        puzzle = perform_analysis(puzzle)
        puzzle, changesd_squares = promote_solved_squares(puzzle)
    
    print("\nAfter attempting to solve\n")
    display_puzzle(puzzle)
    print()

def populate_possible_values(puzzle):
    for x in range(9):
        for y in range(9):
            if puzzle.squares[x][y]['value'] == " ":
                possible_values = list(range(1, 10))
                
                for xaxis in range(9):
                    if (puzzle.squares[xaxis][y]['value'] != " "):
                        possible_values.remove(int(puzzle.squares[xaxis][y]['value']))

                for yaxis in range(9):
                    if (puzzle.squares[x][yaxis]['value'] != " "):
                        if int(puzzle.squares[x][yaxis]['value']) in possible_values:
                            possible_values.remove(int(puzzle.squares[x][yaxis]['value']))
                
                #Check the box
                if 0 <= x <= 2:
                    xrange = [0, 1, 2]
                elif 3 <= x <= 5:
                    xrange = [3, 4, 5]
                else:
                    xrange = [6, 7, 8]
                    
                if 0 <= y <= 2:
                    yrange = [0, 1, 2]
                elif 3 <= y <= 5:
                    yrange = [3, 4, 5]
                else:
                    yrange = [6, 7, 8]
                    
                for xaxis in xrange:
                    for yaxis in yrange:
                        if not (xaxis == x and yaxis == y):
                            if (puzzle.squares[xaxis][yaxis]['value'] != " "):
                                if int(puzzle.squares[xaxis][yaxis]['value']) in possible_values:
                                    possible_values.remove(int(puzzle.squares[xaxis][yaxis]['value']))
                
                puzzle.squares[x][y]['possible_values'] = possible_values
            else:
                puzzle.squares[x][y]['possible_values'] = []

    return puzzle

def prune_possibilities(puzzle):
    for x in range(9):
        for y in range(9):
            found_axis_requirement = False
            found_box_requirement = False
            if puzzle.squares[x][y]['value'] == " ":
                for possible_value in puzzle.squares[x][y]['possible_values']:
                    if not found_axis_requirement and not found_box_requirement:
                        only_x_axis_appearance = True
                        only_y_axis_appearance = True
                        
                        for xaxis in range(9):
                            if possible_value in puzzle.squares[xaxis][y]['possible_values']:
                                only_x_axis_appearance = False

                        for yaxis in range(9):
                            if possible_value in puzzle.squares[x][yaxis]['possible_values']:
                                only_y_axis_appearance = False
                        
                        if only_x_axis_appearance or only_y_axis_appearance:
                            found_axis_requirement = True
                            puzzle.squares[x][y]['possible_values'] = [possible_value]
                        else:
                            only_box_appearance = True
                            #Check the box
                            if 0 <= x <= 2:
                                xrange = [0, 1, 2]
                            elif 3 <= x <= 5:
                                xrange = [3, 4, 5]
                            else:
                                xrange = [6, 7, 8]
                                
                            if 0 <= y <= 2:
                                yrange = [0, 1, 2]
                            elif 3 <= y <= 5:
                                yrange = [3, 4, 5]
                            else:
                                yrange = [6, 7, 8]
                                
                            for xaxis in xrange:
                                for yaxis in yrange:
                                    if not (xaxis == x and yaxis == y):
                                        if possible_value in puzzle.squares[xaxis][yaxis]['possible_values']:
                                            only_box_appearance = False
                                            
                            if only_box_appearance:
                                found_box_requirement = True
                                puzzle.squares[x][y]['possible_values'] = [possible_value]
    return puzzle

def perform_analysis(puzzle):
    # Check if value must appear in the row for possibilities.
    for x in range(9):
        for y in range(9):
            found_match = False
            if puzzle.squares[x][y]['value'] == " ":
                for possible_value in puzzle.squares[x][y]['possible_values']:
                    pass
    
    return puzzle

def promote_solved_squares(puzzle):
    promotions = 0
    
    for x in range(9):
        for y in range(9):
            if len(puzzle.squares[x][y]['possible_values']) == 1:
                puzzle.squares[x][y]['value'] = puzzle.squares[x][y]['possible_values'][0]
                promotions += 1
    
    return puzzle, promotions

class SudokuPuzzle:
    squares = [ [{'value': "", 'possible_values': []} for x in range(9)] for y in range(9)]
    
    def __init__(self):
        pass
    
    def is_valid(self):
        return False
    
    def is_solved(self):
        return False
    
main()
