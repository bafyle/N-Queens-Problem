# import the necessary libraries
import sys
import time

def printBoard(board: list) -> None:
    """ Custom function for printing the board """
    printString = ""
    for i in board:
        for c in i:
            printString += c + " "
        printString += '\n'
    print(printString, end='\n\n')
            

def createBoard(size: int) -> list:
    """
    Returning a 2D list full of dots
    """
    map = list()
    for _ in range(size):
        innerList = ['.'] * size
        map.append(innerList)
    return map

def suitable(row : int, col: int, board: list) -> bool:
    """
    This function checks if a position is suitable to put a queen
    in it or not
    """
    # check row for queens
    ithRow = board[row]
    if 'q' in ithRow:
        return False
    
    # check column for queens
    for i in range(len(board)):
        if board[i][col] == 'q':
            return False

    # check diagonal for queens
    tempRow = row - min(row, col)
    tempCol = col - min(row, col)
    while tempRow < len(board) and tempCol < len(board):
        if board[tempRow][tempCol] == 'q':
            return False
        tempRow += 1
        tempCol += 1
    
    tempRow = row
    tempCol = col
    while tempRow != 0 and tempCol != len(board) - 1:
        tempCol += 1
        tempRow -= 1
    while tempRow < len(board) and tempCol > -1:
        if board[tempRow][tempCol] == 'q':
            return False
        tempRow += 1
        tempCol -= 1
    
    # if no queen detected, then it's a suitable place
    return True

def backtrack(board: list, rowNumber: int, colNumber: int, mapSize: int) -> tuple:
    """
    This function takes the current row and column and tries to backtrack to
    position where there is new possible solution
    return a tuple with the new row and column
    """
    rowNumber -= 1
    colNumber = board[rowNumber].index('q')
    board[rowNumber][colNumber] = '.'
    if colNumber == mapSize - 1:
        rowNumber -= 1
        if rowNumber == -1:
            return -1, -1
        colNumber = board[rowNumber].index('q')
        board[rowNumber][colNumber] = '.'
    colNumber += 1
    return rowNumber, colNumber


def main(args) -> None:
    try:
        boardSize = int(args[1])
    except ValueError:
        print("Passed argument must be an integer")
        sys.exit(1)
    except IndexError:
        boardSize = 4

    foundSolutions = 0
    board = createBoard(boardSize)
    rowNumber = 0
    colNumber = 0
    startTime = time.time()
    while rowNumber >= 0:
        if suitable(rowNumber, colNumber, board):
            board[rowNumber][colNumber] = 'q'
            rowNumber += 1
            colNumber = 0
        elif colNumber != boardSize - 1:
            colNumber += 1
        else:
            rowNumber, colNumber = backtrack(board, rowNumber, colNumber, boardSize)
        if rowNumber >= boardSize:
            printBoard(board)
            rowNumber, colNumber = backtrack(board, rowNumber, colNumber, boardSize)
            foundSolutions += 1
    endTime = time.time()
    if foundSolutions:
        print(f"Execution time: {endTime - startTime}")
    print(f"Found Solutions: {foundSolutions}")

if __name__ == "__main__": # if the file is not imported
    main(sys.argv) # run the main function and pass the arguments
