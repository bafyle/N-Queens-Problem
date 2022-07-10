# import the necessary libraries
import time
import logging
import copy
import argparse
from typing import List, Tuple


def print_solutions_to_console(lists_queue: list) -> None:
    while any(lists_queue):
        printString = ""
        for i in lists_queue[0]:
            for c in i:
                printString += c + ' '
            printString += '\n'
        print(printString, end='\n')
        lists_queue.pop(0)
        


def write_solutions_to_file(lists_queue: list) -> None:
    file = open("output.txt", "w")
    while any(lists_queue):
        printString = ""
        for i in lists_queue[0]:
            for c in i:
                printString += c + ' '
            printString += '\n'
        file.write(printString+'\n')
        lists_queue.pop(0)
    file.flush()
    file.close()
    return
    

def create_board(size: int) -> list:
    """
    Returning a 2D list full of dots
    """
    map = list()
    for _ in range(size):
        innerList = ['.'] * size
        map.append(innerList)
    return map


def is_suitable(row : int, col: int, board: List[List[int]]) -> bool:
    """
    This function checks if a position is suitable to put a queen
    in it or not
    """
    board_size = len(board)

    # check row for queens
    if 'q' in board[row]:
        return False
    
    # check column for queens
    for i in range(board_size):
        if board[i][col] == 'q':
            return False

    # check diagonal for queens

    # left diagonal up
    tmp_row = row - 1
    tmp_col = col - 1
    while tmp_col >= 0 and tmp_row >= 0:
        if board[tmp_row][tmp_col] == 'q':
            return False
        tmp_row -= 1
        tmp_col -= 1

    # left diagonal down
    tmp_row = row + 1
    tmp_col = col + 1
    while tmp_row < board_size and tmp_col < board_size:
        if board[tmp_row][tmp_col] == 'q':
            return False
        tmp_row += 1
        tmp_col += 1

    # right diagonal up
    tmp_row = row - 1
    tmp_col = col + 1
    while tmp_row < board_size and tmp_col < board_size:
        if board[tmp_row][tmp_col] == 'q':
            return False
        tmp_row -= 1
        tmp_col += 1

    # right diagonal down
    tmp_row = row + 1
    tmp_col = col - 1
    while tmp_row < board_size and tmp_col < board_size:
        if board[tmp_row][tmp_col] == 'q':
            return False
        tmp_row += 1
        tmp_col -= 1
    return True


def backtrack(board: List[List[int]], rowNumber: int, colNumber: int) -> tuple:
    """
    This function takes the current row and column and tries to backtrack to
    position where there is new possible solution
    return a tuple with the new row and column
    """
    board_size = len(board)
    rowNumber -= 1
    colNumber = board[rowNumber].index('q')
    board[rowNumber][colNumber] = '.'
    if colNumber == board_size - 1:
        rowNumber -= 1
        if rowNumber == -1:
            return -1, -1
        colNumber = board[rowNumber].index('q')
        board[rowNumber][colNumber] = '.'
    colNumber += 1
    return rowNumber, colNumber


def prepare_arguments_parser(**kwargs) -> argparse.ArgumentParser:
    args_parser = argparse.ArgumentParser(description=kwargs["description"], allow_abbrev=False)
    args_parser.add_argument(
        '-s',
        '--size',
        required=False,
        type=int,
        help='specifying the size of the board',
    )
    args_parser.add_argument(
        '-f',
        '--file',
        required=False,
        help='create a text file with all solutions',
        action='store_true'
    )
    args_parser.add_argument(
        '-c',
        '--console',
        required=False,
        help='print all solutions to the console',
        action='store_true'
    )
    return args_parser


def confirming_printing_solutions_to_terminal(no_of_solutions: int):
    if no_of_solutions > 100:
        logging.info("Printing all solutions may take a lot of time are you sure ? (y/N)")
        user_input = input().lower()
        while user_input != 'y' and user_input != 'n':
            print("Answer with y for yes and n for no")
            user_input = input().lower()
        return True if user_input == 'y' else False
    return True

def creating_and_solving_board(board_size: int) -> Tuple[list, int]:
    
    solved_puzzles_list = []
    board = create_board(board_size)
    solutions_found = 0
    row_number = 0
    col_number = 0
    while row_number >= 0:
        if is_suitable(row_number, col_number, board):
            board[row_number][col_number] = 'q'
            row_number += 1
            col_number = 0
        elif col_number != board_size - 1:
            col_number += 1
        else:
            row_number, col_number = backtrack(board, row_number, col_number)
        if row_number >= board_size:
            solved_puzzles_list.append(copy.deepcopy(board))
            row_number, col_number = backtrack(board, row_number, col_number)
            solutions_found += 1
    return solved_puzzles_list, solutions_found

def main() -> None:
    logging.basicConfig(format='%(message)s', level=logging.INFO)

    args_parser = prepare_arguments_parser(description="Solving the N Queen problem")
    
    parsed_args = args_parser.parse_args()
    board_size = 4 if parsed_args.size is None else parsed_args.size

    exe_start_time = time.perf_counter()
    solved_puzzles_list, solutions_found = creating_and_solving_board(board_size)
    exe_end_time = time.perf_counter()

    if solutions_found:
        logging.info(f"Execution time: {exe_end_time - exe_start_time}")
    logging.info(f"Found Solutions: {solutions_found}")
    if parsed_args.file:
        logging.info("Writing solutions to a text file...")
        write_solutions_to_file(solved_puzzles_list)
        logging.info("Done")
    elif parsed_args.console:
        confirmation = confirming_printing_solutions_to_terminal(solutions_found)
        if confirmation == False: return
        logging.info("Printing solutions...")
        print_solutions_to_console(solved_puzzles_list)
        logging.info("Finished printing solutions.")


if __name__ == "__main__":
    main()
