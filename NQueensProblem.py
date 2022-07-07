# import the necessary libraries
import time
import logging
import copy
import argparse
from typing import List

lists_queue = []


def print_solutions_to_console() -> None:
    global lists_queue
    while any(lists_queue):
        printString = ""
        for i in lists_queue[0]:
            for c in i:
                printString += c + ' '
            printString += '\n'
        print(printString, end='\n')
        lists_queue.pop(0)
        


def write_solutions_to_file() -> None:
    global lists_queue
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
    

def createBoard(size: int) -> list:
    """
    Returning a 2D list full of dots
    """
    map = list()
    for _ in range(size):
        innerList = ['.'] * size
        map.append(innerList)
    return map

def suitable(row : int, col: int, board: List[List[int]]) -> bool:
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


def main() -> None:
    global is_solving_puzzles_finished
    logging.basicConfig(format='%(message)s', level=logging.INFO)

    arguments_prs = argparse.ArgumentParser(description="Solving the N Queen problem", allow_abbrev=False)
    arguments_prs.add_argument(
        '-s',
        '--size',
        required=False,
        type=int,
        help='Specifying the size of the board',
    )
    arguments_prs.add_argument(
        '-f',
        '--file',
        required=False,
        help='Create a text file with all solutions',
        action='store_true'
    )
    arguments_prs.add_argument(
        '-c',
        '--console',
        required=False,
        help='print all solutions to the console',
        action='store_true'
    )

    parsed_args = arguments_prs.parse_args()
    board_size = 4 if parsed_args.size is None else parsed_args.size

    board = createBoard(board_size)
    solutions_found = 0
    row_number = 0
    col_number = 0
    exe_start_time = time.perf_counter()
    while row_number >= 0:
        if suitable(row_number, col_number, board):
            board[row_number][col_number] = 'q'
            row_number += 1
            col_number = 0
        elif col_number != board_size - 1:
            col_number += 1
        else:
            row_number, col_number = backtrack(board, row_number, col_number)
        if row_number >= board_size:
            lists_queue.append(copy.deepcopy(board))
            row_number, col_number = backtrack(board, row_number, col_number)
            solutions_found += 1
    exe_end_time = time.perf_counter()
    if solutions_found:
        logging.info(f"Execution time: {exe_end_time - exe_start_time}")
    logging.info(f"Found Solutions: {solutions_found}")
    if parsed_args.file:
        logging.info("Writing solutions to a text file...")
        write_solutions_to_file()
        logging.info("Done")
    elif parsed_args.console:
        logging.info("Printing solutions...")
        print_solutions_to_console()
        logging.info("Done")


if __name__ == "__main__": # if the file is not imported
    main() # run the main function and pass the arguments
