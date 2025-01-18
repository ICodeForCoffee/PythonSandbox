import numpy
import copy

def main():
    puzzle = load_puzzle("sudoku-puzzle4.txt")
    print("Initial puzzle\n")
    display_puzzle(puzzle)
    solve_puzzle(puzzle)
    print("After attempting to solve\n")
    display_puzzle(puzzle)
    print(f"This puzzle is {"solved" if puzzle.is_solved() == True else "unsolved"}")
    print()


def load_puzzle(fila_name):
    file = open(fila_name, "r")
    puzzle = SudokuPuzzle()
    
    for x in range(9):
        line = file.readline()
        line = line.replace("|", "")
        
        for y in range(9):
            puzzle.squares[x][y]['value'] = line[y]
        
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
    print("")

def solve_puzzle(puzzle):
    changesd_squares = 1
    
    while changesd_squares > 0:
        changesd_squares = 0
        populate_possible_values(puzzle)
        prune_possibilities(puzzle)
        perform_analysis(puzzle)
        changesd_squares = promote_solved_squares(puzzle)
    
    if not puzzle.is_solved():
        guess_a_value(puzzle)
    return puzzle

def populate_possible_values(puzzle):
    for x in range(9):
        for y in range(9):
            if puzzle.squares[x][y]['value'] == " ":
                possible_values = list(range(1, 10))
                
                for xaxis in range(9):
                    if (puzzle.squares[xaxis][y]['value'] != " "):
                        if int(puzzle.squares[xaxis][y]['value']) in possible_values:
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

def perform_analysis(puzzle):
    #thre is another case I can check here for solving the puzzle.
    # I need to check if values for a cell must appear in other cells aligned with the cell on the x asxis and the yaxis. If so, I can prune the list of possibilities
    # Specifically, the use case of two values must appear in two specific cells on any axis.
    # I could also look at this for three cells in a box one the axises.
    pass
    
def guess_a_value(puzzle):
    # Check if value must appear in the row for possibilities.
    # Or for the moment we'll cheat
    unmodified_puzzle = copy.deepcopy(puzzle )
    
    for x in range(9):
        for y in range(9):
            if puzzle.squares[x][y]['value'] == " ": #I could check here that the possible value list is not empty
                for possible_value in puzzle.squares[x][y]['possible_values']:
                    print(f"Guessing a value at [{x}, {y}]") #added for debugging.
                    print()
                    display_puzzle(puzzle)
                    
                    puzzle_copy = copy.deepcopy(unmodified_puzzle )
                    puzzle_copy.squares[x][y]['value'] = possible_value
                    puzzle_copy = solve_puzzle(puzzle_copy)
                    if puzzle_copy.is_solved():
                        return puzzle_copy
    
    return unmodified_puzzle

def promote_solved_squares(puzzle):
    promotions = 0
    
    for x in range(9):
        for y in range(9):
            if len(puzzle.squares[x][y]['possible_values']) == 1:
                puzzle.squares[x][y]['value'] = puzzle.squares[x][y]['possible_values'][0]
                promotions += 1
    
    return promotions

class SudokuPuzzle:
    squares = [ [{'value': "", 'possible_values': []} for x in range(9)] for y in range(9)]
    
    def __init__(self):
        pass
    
    # def is_valid(self):
    #     value_list = list(range(1, 10))
    #     for x in range(9):
    #         found_values = []
    #         for y in range(9):
    #             if self.squares[x][y]['value'] == " ":
    #                 return False
                
    #             found_values.append(int(self.squares[x][y]['value']))
    #         found_values.sort()
            
    #         if value_list != found_values:
    #             return False
            
    #     for y in range(9):
    #         found_values = []
    #         for x in range(9):
    #             if self.squares[x][y]['value'] == " ":
    #                 return False
                
    #             found_values.append(int(self.squares[x][y]['value']))
    #         found_values.sort()
            
    #         if value_list != found_values:
    #             return False
            
    #     return True
    
    def is_solved(self):
        for x in range(9):
            for y in range(9):
                if self.squares[x][y]['value'] == " ":
                    return False
        
                value_list = list(range(1, 10))

        for x in range(9):
            found_values = []
            for y in range(9):
                if self.squares[x][y]['value'] == " ":
                    return False
                
                found_values.append(int(self.squares[x][y]['value']))
            found_values.sort()
            
            if value_list != found_values:
                return False
            
        for y in range(9):
            found_values = []
            for x in range(9):
                if self.squares[x][y]['value'] == " ":
                    return False
                
                found_values.append(int(self.squares[x][y]['value']))
            found_values.sort()
            
            if value_list != found_values:
                return False
            
        return True

main()