from SudokuPuzzle import SudokuPuzzle
import copy

class SudokuSolver:
    def __init__(self):
        pass

    def load_puzzle(self, file_name):
        file = open(file_name, "r")
        puzzle = SudokuPuzzle()

        for x in range(9):
            line = file.readline()
            if line[0] == "-":
                line = file.readline()
            line = line.replace("|", "")

            for y in range(9):
                puzzle.squares[x][y]['value'] = line[y]

        return puzzle

    def display_puzzle(self, puzzle):
        for x in range(9):
            if x == 3 or x == 6:
                print("--------- --------- ---------")
            for y in range(9):
                if y == 3 or y == 6:
                    print("|", end="")
                print(f" {puzzle.squares[x][y]['value']} ", end="")

            print("")
        print("")

    def solve_puzzle(self, puzzle):
        changesd_squares = 1

        while changesd_squares > 0:
            changesd_squares = 0
            self.populate_possible_values(puzzle)
            self.prune_possibilities(puzzle)
            self.perform_analysis(puzzle)
            changesd_squares = self.promote_solved_squares(puzzle)

        if not puzzle.is_solved():
            puzzle = self.guess_a_value(puzzle)
        
        return puzzle

    def populate_possible_values(self, puzzle):
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

    def prune_possibilities(self, puzzle):
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

    def perform_analysis(self, puzzle):
        #thre is another case I can check here for solving the puzzle.
        # I need to check if values for a cell must appear in other cells aligned with the cell on the x asxis and the yaxis. If so, I can prune the list of possibilities
        # Specifically, the use case of two values must appear in two specific cells on any axis.
        # I could also look at this for three cells in a box one the axises.
        pass

    def guess_a_value(self, puzzle):
        # Check if value must appear in the row for possibilities.
        # Or for the moment we'll cheat
        puzzle.guessing_used = True
        unmodified_puzzle = copy.deepcopy(puzzle)

        x, y = self.pick_a_square_to_guess(unmodified_puzzle)

        for possible_value in unmodified_puzzle.squares[x][y]['possible_values']:
            #print(f"Guessing a value at [{x}, {y}] with the value {possible_value}") #added for debugging.
            #print()
            puzzle2 = copy.deepcopy(unmodified_puzzle)

            #display_puzzle(puzzle2)

            puzzle2.squares[x][y]['value'] = possible_value
            self.populate_possible_values(puzzle2)
            self.prune_possibilities(puzzle2)

            puzzle2 = self.solve_puzzle(puzzle2)
            if puzzle2.is_solved():
                puzzle = copy.deepcopy(puzzle2)
                return puzzle
      
        return unmodified_puzzle

    def pick_a_square_to_guess(self, puzzle):
        #If there is a square with only one option, this method should not be called, but we're returning it incase it is.
        for option_count in range(2, 10):
            for x in range(9):
                for y in range(9):
                    if puzzle.squares[x][y]['value'] == " " and len(puzzle.squares[x][y]['possible_values']) > 0 and len(puzzle.squares[x][y]['possible_values']) <= option_count:
                        return x, y
        
        #This is an error state
        return -1, -1

    def promote_solved_squares(self, puzzle):
        promotions = 0

        for x in range(9):
            for y in range(9):
                if len(puzzle.squares[x][y]['possible_values']) == 1:
                    puzzle.squares[x][y]['value'] = puzzle.squares[x][y]['possible_values'][0]
                    promotions += 1

        return promotions