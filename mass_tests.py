from sudoku_class import Sudoku
from solver_class import Solver
import time
import os


def print_stats(stats_list):
    logfile = 'test_log_file ' + stats_list[0][0] + ' ' + time.ctime() + '.txt'
    output_file_opened = open(logfile, 'w+')
    output_string = ''
    rolling_sum = 0
    rolling_count = 0
    output_string = output_string + '\n'
    output_string = output_string + ' -' * 30 + '\n'
    for i in stats_list:
        rolling_sum += i[1]
        rolling_count += 1
        output_string = output_string + '|' + \
            i[0].center(18) + '|  ' + '{} nodes'.format(str(i[2])).ljust(13) + '| ' + str(i[1]).ljust(23) + '|' + '\n'
    output_string = output_string + ' -' * 30 + '\n'
    output_string = output_string + '|' + \
        'Total processes : {}'.format(rolling_count).center(59) + '|' + '\n'
    output_string = output_string + '|' + \
        'Total time of process : {}'.format(
            rolling_sum).center(59) + '|' + '\n'
    output_string = output_string + '|' + \
        'Average time of process : {}'.format(
            rolling_sum / rolling_count).center(59) + '|' + '\n'
    output_string = output_string + ' -' * 30 + '\n'

    output_file_opened.write(output_string)
    output_file_opened.close()


test_files = {
    'basic_tests': 'input/p096_sudoku.txt',
    'level_0': 'input/0.txt',
    'level_1': 'input/1.txt',
    'level_2': 'input/2.txt',
    'level_3': 'input/3.txt',
    'level_5': 'input/5.txt'
}

solve_method = int(input(' Solve methods: \n \
                         Brute Force > 0 \n \
                         BF Graphic  > 1 \n \
                         Best Guess  > 2 \n \
                         BG Graphic  > 3 \n \
                         BG Improvd  > 4 \n \
                         BF/G Hybrid > 5 \n \
                         Selective   > 6 \n \n \
                         Choose method ? '))


for i in test_files.keys():
    stats_list = []
    index_file = 0
    if input(' Test with {} files ? : '.format(i)) != 'y':
        break
    workfile = test_files[i]
    input_file_opened = open(workfile, 'r')
    for line in input_file_opened:
        os.system('clear')
        this_sudoku_stats = []
        time_at_start = time.time()
        index_file += 1
        sudoku_map_to_import = [int(x) for x in line if x != '\n']
        this_sudoku = Sudoku(sudoku_map_to_import)
        print()
        print(' Sudoku provided : ')
        this_sudoku.display()
        sudoku_solved = Solver()
        [fully_solved, walked_path, walked_lenght] = sudoku_solved.solve(
            this_sudoku.sudoku_map, solve_method)
        time_at_end = time.time()
        print('\n', 'Solved :')
        end_sudoku = Sudoku(fully_solved)
        end_sudoku.display()
        print('\n', 'Time elapsed: {} seconds'.format(
            time_at_end - time_at_start))
        # print('\n', 'Path walked : {}'.format(walked_path)
        print('\n', 'Path lenght : {}'.format(walked_lenght))
        print()
        this_sudoku_stats.append(str(i) + ' ' + str(index_file))
        this_sudoku_stats.append(time_at_end - time_at_start)
        this_sudoku_stats.append(walked_lenght)
        stats_list.append(this_sudoku_stats)
    input_file_opened.close()
    print_stats(stats_list)
