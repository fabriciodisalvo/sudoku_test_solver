from sudoku_class import Sudoku
from solver_class import Solver
import time

def print_stats(stats_list):
    rolling_sum = 0
    rolling_count = 0
    print()
    print(' -' * 30)
    for i in stats_list:
        rolling_sum += i[1]
        rolling_count += 1
        print("|", i[0].center(15), "|",
                "{} nodes".format(str(i[2])).ljust(13), "|",
                str(i[1]).ljust(23), "|")
    print(' -' * 30)
    print("|", 'Total processes : {}'.format(rolling_count).center(57), "|")
    print("|", 'Total time of process : {}'.format(rolling_sum).center(57), "|")
    print("|", 'Average time of process : {}'.format(rolling_sum / rolling_count).center(57), "|")
    print(' -' * 30)
    print()

sudoku_map_list = {
    'real_test': [0, 0, 0, 0, 0, 4, 0, 9, 0,
                  8, 0, 2, 9, 7, 0, 0, 0, 0,
                  9, 0, 1, 2, 0, 0, 3, 0, 0,
                  0, 0, 0, 0, 4, 9, 1, 5, 7,
                  0, 1, 3, 0, 5, 0, 9, 2, 0,
                  5, 7, 9, 1, 2, 0, 0, 0, 0,
                  0, 0, 7, 0, 0, 2, 6, 0, 3,
                  0, 0, 0, 0, 3, 8, 2, 0, 5,
                  0, 2, 0, 5, 0, 0, 0, 0, 0]
}

stats_list = []


solve_method = int(input(' Solve methods: \n Brute Force > 0 \n BF Graphic  > 1 \n Best Guess  > 2 \n BG Graphic  > 3 \n BG Improvd  > 4 \n  \n Choose method ? '))

for i in sudoku_map_list.keys():
    this_sudoku_stats = []
    time_at_start = time.time()
    this_sudoku = Sudoku(sudoku_map_list[i])
    print()
    print(' Sudoku provided : ')
    this_sudoku.display()
    sudoku_solved = Solver()
    [fully_solved, walked_path, walked_lenght] = sudoku_solved.solve(this_sudoku.sudoku_map, solve_method)
    time_at_end = time.time()
    print('\n', 'Solved :')
    end_sudoku = Sudoku(fully_solved)
    end_sudoku.display()
    print('\n', 'Time elapsed: {} seconds'.format(
            time_at_end - time_at_start
          ))
    # print('\n', 'Path walked : {}'.format(walked_path)
    print('\n', 'Path lenght : {}'.format(walked_lenght))
    print()
    this_sudoku_stats.append(i)
    this_sudoku_stats.append(time_at_end - time_at_start)
    this_sudoku_stats.append(walked_lenght)
    stats_list.append(this_sudoku_stats)

print_stats(stats_list)
