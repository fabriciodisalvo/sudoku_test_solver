from sudoku_class import Sudoku
import os


class Solver:
    def __init__(self):
        self.path_list = []
        self.possible_guesses = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.related_groups_dictionary = {}

    def find_related_groups(self, location):
        current_line_to_check = list(range(((location // 9) * 9), ((location // 9) * 9 + 9)))
        squares = [[0, 1, 2, 9, 10, 11, 18, 19, 20],
                   [3, 4, 5, 12, 13, 14, 21, 22, 23],
                   [6, 7, 8, 15, 16, 17, 24, 25, 26],
                   [27, 28, 29, 36, 37, 38, 45, 46, 47],
                   [30, 31, 32, 39, 40, 41, 48, 49, 50],
                   [33, 34, 35, 42, 43, 44, 51, 52, 53],
                   [54, 55, 56, 63, 64, 65, 72, 73, 74],
                   [57, 58, 59, 66, 67, 68, 75, 76, 77],
                   [60, 61, 62, 69, 70, 71, 78, 79, 80]]
        for square in squares:
            if location in square:
                current_square_to_check = square
        current_column_to_check = [num for num in range(81) if num % 9 == location % 9]
        all_relatives = current_line_to_check
        for x in current_column_to_check:
            if x not in all_relatives:
                all_relatives.append(x)
        for y in current_square_to_check:
            if y not in all_relatives:
                all_relatives.append(y)
        all_relatives.remove(location)
        return(all_relatives)

    def solve_version_01(self, sudoku_input_map):
        sudoku_map = sudoku_input_map
        try:
            last_changed_position = sudoku_map.index(0)
            all_relatives = self.find_related_groups(last_changed_position)
            all_relative_values = [sudoku_map[x] for x in all_relatives]
            possible_guesses_for_this_location = [x for x in self.possible_guesses if x not in all_relative_values]
            if len(possible_guesses_for_this_location) > 0:
                for x in possible_guesses_for_this_location:
                    self.path_list.append(last_changed_position + 1)
                    sudoku_map[last_changed_position] = x
                    if self.solve_version_01(sudoku_map):
                        return [sudoku_map, self.path_list, len(self.path_list)]
                sudoku_map[last_changed_position] = 0
            else:
                sudoku_map[last_changed_position] = 0
        except ValueError:
            return [sudoku_map, self.path_list, len(self.path_list)]

    def solve_version_01_graphic(self, sudoku_input_map):
        sudoku_map = sudoku_input_map
        try:
            last_changed_position = sudoku_map.index(0)
            all_relatives = self.find_related_groups(last_changed_position)
            all_relative_values = [sudoku_map[x] for x in all_relatives]
            possible_guesses_for_this_location = [x for x in self.possible_guesses if x not in all_relative_values]
            if len(possible_guesses_for_this_location) > 0:
                for x in possible_guesses_for_this_location:
                    self.path_list.append(last_changed_position + 1)
                    sudoku_map[last_changed_position] = x
                    os.system('clear')  # CONSOLE PROGRESS DYNAMIC VIEW
                    print('\n', 'Testing values :')  # CONSOLE PROGRESS DYNAMIC VIEW
                    Sudoku(sudoku_map).display()  # CONSOLE PROGRESS DYNAMIC VIEW
                    print(' Path lenght : {}'.format(len(self.path_list)))  # CONSOLE PROGRESS DYNAMIC VIEW
                    print(' Position : {} ;  Possible values : {}'.format(last_changed_position, possible_guesses_for_this_location))  # remove after testing
                    print(' Setting {} in position {}'.format(x, last_changed_position))  # remove after testing
                    print()
                    sudoku_map[last_changed_position] = x
                    if self.solve_version_01_graphic(sudoku_map):
                        return [sudoku_map, self.path_list, len(self.path_list)]
                print(' Position : {}'.format(last_changed_position))  # remove after testing
                print(' Exhausted all choices for this position. Backtracking...')  # remove after testing
                sudoku_map[last_changed_position] = 0  # LATEST TESTING
                print()
            else:
                print(' Position : {}'.format(last_changed_position))  # remove after testing
                print(' No valid options for this position, backtracking...')  # remove after testing
                sudoku_map[last_changed_position] = 0  # LATEST TESTING
                print()
        except ValueError:
            return [sudoku_map, self.path_list, len(self.path_list)]

    def solve_version_02(self, sudoku_input_map):
        sudoku_map = sudoku_input_map
        blank_indices = [i for i, x in enumerate(sudoku_map) if x == 0]
        if len(blank_indices) == 0:
                return [sudoku_map, self.path_list, len(self.path_list)]
        most_relevant_position = 0
        most_relevant_position_options = [None, None, None, None, None, None, None, None, None, None]
        for position in blank_indices:
            all_relatives = self.find_related_groups(position)
            all_relative_values = [sudoku_map[x] for x in all_relatives]
            possible_guesses_for_this_location = [x for x in self.possible_guesses if x not in all_relative_values]
            if len(possible_guesses_for_this_location) < len(most_relevant_position_options):
                most_relevant_position = position
                most_relevant_position_options = possible_guesses_for_this_location
        if len(most_relevant_position_options) > 0:
            for x in most_relevant_position_options:
                self.path_list.append(most_relevant_position + 1)
                sudoku_map[most_relevant_position] = x
                if self.solve_version_02(sudoku_map):
                    return [sudoku_map, self.path_list, len(self.path_list)]
            sudoku_map[most_relevant_position] = 0
        else:
            sudoku_map[most_relevant_position] = 0

    def solve_version_02_graphic(self, sudoku_input_map):
        sudoku_map = sudoku_input_map
        blank_indices = [i for i, x in enumerate(sudoku_map) if x == 0]
        if len(blank_indices) == 0:
                return [sudoku_map, self.path_list, len(self.path_list)]
        most_relevant_position = 0
        most_relevant_position_options = [None, None, None, None, None, None, None, None, None, None]
        for position in blank_indices:
            all_relatives = self.find_related_groups(position)
            all_relative_values = [sudoku_map[x] for x in all_relatives]
            possible_guesses_for_this_location = [x for x in self.possible_guesses if x not in all_relative_values]
            if len(possible_guesses_for_this_location) < len(most_relevant_position_options):
                most_relevant_position = position
                most_relevant_position_options = possible_guesses_for_this_location
        if len(most_relevant_position_options) > 0:
            for x in most_relevant_position_options:
                self.path_list.append(most_relevant_position + 1)
                sudoku_map[most_relevant_position] = x
                os.system('clear')  # CONSOLE PROGRESS DYNAMIC VIEW
                print('\n', 'Testing values :')  # CONSOLE PROGRESS DYNAMIC VIEW
                Sudoku(sudoku_map).display()  # CONSOLE PROGRESS DYNAMIC VIEW
                print(' Path lenght : {}'.format(len(self.path_list)))  # CONSOLE PROGRESS DYNAMIC VIEW
                print(' Position : {} ;  Possible values : {}'.format(most_relevant_position, most_relevant_position_options))  # remove after testing
                print(' Setting {} in position {}'.format(x, most_relevant_position))  # remove after testing
                print()
                if self.solve_version_02_graphic(sudoku_map):
                    return [sudoku_map, self.path_list, len(self.path_list)]
            sudoku_map[most_relevant_position] = 0
            print(' Position : {}'.format(most_relevant_position))  # remove after testing
            print(' Exhausted all choices for this position. Backtracking...')  # remove after testing
            sudoku_map[most_relevant_position] = 0  # LATEST TESTING
            print()
        else:
            sudoku_map[most_relevant_position] = 0
            print(' Position : {}'.format(most_relevant_position))  # remove after testing
            print(' No valid options for this position, backtracking...')  # remove after testing
            sudoku_map[most_relevant_position] = 0  # LATEST TESTING
            print()

    def solve_version_03(self, sudoku_input_map):
        sudoku_map = sudoku_input_map
        blank_indices = [i for i, x in enumerate(sudoku_map) if x == 0]
        if len(blank_indices) == 0:
                return [sudoku_map, self.path_list, len(self.path_list)]
        most_relevant_position = 0
        most_relevant_position_options = [None, None, None, None, None, None, None, None, None, None]
        for position in blank_indices:
            if position in self.related_groups_dictionary:
                pass
            else:
                self.related_groups_dictionary[position] = self.find_related_groups(position)
            all_relative_values = [sudoku_map[x] for x in self.related_groups_dictionary[position]]
            possible_guesses_for_this_location = [x for x in self.possible_guesses if x not in all_relative_values]
            if len(possible_guesses_for_this_location) < len(most_relevant_position_options):
                most_relevant_position = position
                most_relevant_position_options = possible_guesses_for_this_location
        if len(most_relevant_position_options) > 0:
            for x in most_relevant_position_options:
                self.path_list.append(most_relevant_position + 1)
                sudoku_map[most_relevant_position] = x
                if self.solve_version_03(sudoku_map):
                    return [sudoku_map, self.path_list, len(self.path_list)]
            sudoku_map[most_relevant_position] = 0
        else:
            sudoku_map[most_relevant_position] = 0

    def solve_hybrid(self, sudoku_input_map):
        sudoku_map = sudoku_input_map
        try:
            last_changed_position = sudoku_map.index(0)
            all_relatives = self.find_related_groups(last_changed_position)
            all_relative_values = [sudoku_map[x] for x in all_relatives]
            possible_guesses_for_this_location = [x for x in self.possible_guesses if x not in all_relative_values]
            if len(possible_guesses_for_this_location) > 0:
                for x in possible_guesses_for_this_location:
                    self.path_list.append(last_changed_position + 1)
                    sudoku_map[last_changed_position] = x
                    if len(self.path_list) > 100:
                        if self.solve_version_03(sudoku_map):
                            return [sudoku_map, self.path_list, len(self.path_list)]
                    else:
                        if self.solve_hybrid(sudoku_map):
                            return [sudoku_map, self.path_list, len(self.path_list)]
                sudoku_map[last_changed_position] = 0
            else:
                sudoku_map[last_changed_position] = 0
        except ValueError:
            return [sudoku_map, self.path_list, len(self.path_list)]

    def solve(self, sudoku_input_map, solve_method=4):
        if solve_method == 0:
            return self.solve_version_01(sudoku_input_map)
        elif solve_method == 1:
            return self.solve_version_01_graphic(sudoku_input_map)
        elif solve_method == 2:
            return self.solve_version_02(sudoku_input_map)
        elif solve_method == 3:
            return self.solve_version_02_graphic(sudoku_input_map)
        elif solve_method == 4:
            return self.solve_version_03(sudoku_input_map)
        elif solve_method == 5:
            return self.solve_hybrid(sudoku_input_map)
        elif solve_method == 6:
            blank_indices = [i for i, x in enumerate(sudoku_input_map) if x == 0]
            if len(blank_indices) < 46:
                return self.solve_version_01(sudoku_input_map)
            else:
                return self.solve_version_03(sudoku_input_map)
        else:
            print('Not a valid solve method')
